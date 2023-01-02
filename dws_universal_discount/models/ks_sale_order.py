# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api, _
from functools import partial
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import formatLang

_logger = logging.getLogger(__name__)

class KsGlobalDiscountSales(models.Model):
    _inherit = "sale.order"

    ks_global_discount_type = fields.Selection([('percent', 'Percentage'), ('amount', 'Amount')],
                                               string='Order Discount Type',
                                               readonly=True,
                                               states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                                               default='percent')
    ks_global_discount_rate = fields.Float('Order Discount',
                                           readonly=True,
                                           states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    ks_amount_discount = fields.Monetary(string='Order Discount', readonly=True, compute='_amount_all', store=True,
                                         track_visibility='always')
    ks_enable_discount = fields.Boolean(compute='ks_verify_discount')
    ks_rate = fields.Float(default=0.0)

    discount_total = fields.Monetary("Line Discount Total", compute='total_discount')
    total_untaxed = fields.Monetary(string='Total Untaxed Amount', readonly=True)

    # Count for total discount
    @api.depends('order_line.product_uom_qty', 'order_line.price_unit', 'order_line.discount')
    def total_discount(self):
        for order in self:
            total_price = 0
            discount_amount = 0
            final_discount_amount = 0
            if order:
                for line in order.order_line:
                    if line:
                        total_price = line.product_uom_qty * line.price_unit
                        if total_price:
                            discount_amount = total_price - line.price_subtotal
                            if discount_amount:
                                final_discount_amount = final_discount_amount + discount_amount
                # final_discount_amount = final_discount_amount + self.ks_amount_discount
                order.update({'discount_total': final_discount_amount})

    @api.depends('company_id.ks_enable_discount')
    def ks_verify_discount(self):
        for rec in self:
            rec.ks_enable_discount = rec.company_id.ks_enable_discount

    @api.depends('order_line.price_total', 'ks_global_discount_rate', 'ks_global_discount_type')
    def _amount_all(self):
        res = super(KsGlobalDiscountSales, self)._amount_all()
        for rec in self:
            if not ('ks_global_tax_rate' in rec):
                rec.ks_calculate_discount()
        return res

    # @api.multi
    def _prepare_invoice(self):
        res = super(KsGlobalDiscountSales, self)._prepare_invoice()
        for rec in self:
            res['ks_global_discount_rate'] = rec.ks_global_discount_rate
            res['ks_global_discount_type'] = rec.ks_global_discount_type
        return res

    # @api.multi
    def ks_calculate_discount(self):
        for rec in self:
            if rec.ks_global_discount_type == "amount":
                rec.ks_amount_discount = rec.ks_global_discount_rate if rec.amount_untaxed > 0 else 0

            elif rec.ks_global_discount_type == "percent":
                if rec.ks_global_discount_rate != 0.0:
                    # pkr: removed amount tax
                    rec.ks_amount_discount = (rec.amount_untaxed) * rec.ks_global_discount_rate / 100
                else:
                    rec.ks_amount_discount = 0
            elif not rec.ks_global_discount_type:
                rec.ks_amount_discount = 0
                rec.ks_global_discount_rate = 0
            if rec.ks_global_discount_type == 'amount':
                rec.ks_rate = rec.ks_amount_discount / rec.amount_untaxed
            elif rec.ks_global_discount_type == 'percent':
                rec.ks_rate = rec.ks_global_discount_rate / 100
            rec.total_untaxed = rec.amount_untaxed - rec.ks_amount_discount
            rec.amount_tax *= (1 - rec.ks_rate)
            rec.amount_total = rec.amount_untaxed + rec.amount_tax - rec.ks_amount_discount

    @api.constrains('ks_global_discount_rate')
    def ks_check_discount_value(self):
        if self.ks_global_discount_type == "percent":
            if self.ks_global_discount_rate > 100 or self.ks_global_discount_rate < 0:
                raise ValidationError('You cannot enter percentage value greater than 100.')
        else:
            if self.ks_global_discount_rate < 0 or self.ks_global_discount_rate > self.amount_untaxed:
                raise ValidationError(
                    'You cannot enter discount amount greater than actual cost or value lower than 0.')

    def _amount_by_group(self):
        for order in self:
            currency = order.currency_id or order.company_id.currency_id
            fmt = partial(formatLang, self.with_context(lang=order.partner_id.lang).env, currency_obj=currency)
            res = {}
            for line in order.order_line:
                price_reduce = line.price_unit * (1.0 - line.discount / 100.0)
                taxes = line.tax_id.compute_all(price_reduce, quantity=line.product_uom_qty, product=line.product_id, partner=order.partner_shipping_id)['taxes']
                for tax in line.tax_id:
                    group = tax.tax_group_id
                    res.setdefault(group, {'amount': 0.0, 'base': 0.0})
                    for t in taxes:
                        if t['id'] == tax.id or t['id'] in tax.children_tax_ids.ids:
                            res[group]['amount'] += (t['amount'] * (1 - order.ks_rate))
                            res[group]['base'] += (t['base'] * (1 - order.ks_rate))
            res = sorted(res.items(), key=lambda l: l[0].sequence)
            order.amount_by_group = [(
                l[0].name, l[1]['amount'], l[1]['base'],
                fmt(l[1]['amount']), fmt(l[1]['base']),
                len(res),
            ) for l in res]

    @api.depends('order_line.margin', 'amount_untaxed', 'ks_rate')
    def _compute_margin(self):
        res = super(KsGlobalDiscountSales, self)._compute_margin()
        for order in self:
            margin = 0.0
            for line in order.order_line:
                if line.state != 'cancel':
                    margin += ((line.price_subtotal * (1 - order.ks_rate)) - (line.purchase_price * line.product_uom_qty))
            order.margin = margin
            order.margin_percent = order.amount_untaxed and order.margin / order.total_untaxed
        return res

class KsSaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange("tax_id")
    def onchange_tax_id(self):
        sale_tax_id = self.env.company.ks_sales_tax
        if self.tax_id and (len(self.tax_id) > 1 \
                or (sale_tax_id.id != self.tax_id[0].id.origin
                                                    and self.env["account.tax"].search([('id', '=', self.tax_id[0].id.origin)], limit=1).amount != 0.0)):
            raise ValidationError(_("Tax should be '%s' as set in Accounting settings or set to zero." % sale_tax_id.name))


class KsSaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoice(self, order, so_line, amount):
        invoice = super(KsSaleAdvancePaymentInv, self)._create_invoice(order, so_line, amount)
        if invoice:
            invoice['ks_global_discount_rate'] = order.ks_global_discount_rate
            invoice['ks_global_discount_type'] = order.ks_global_discount_type
        return invoice
