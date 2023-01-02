# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleCustomInvoiceAll(models.Model):
    _inherit = 'sale.order'

    all_to_invoice = fields.Boolean(compute='_all_to_invoice', store=True)

    @api.depends('state', 'order_line.invoice_status')
    def _all_to_invoice(self):
        for rec in self:
            invoice = False
            if len(rec.order_line) > 0:
                invoice = True
                for sale_order_line in rec.order_line:
                    if sale_order_line.invoice_status != 'to invoice':
                        invoice = False
            print('invoice all =', invoice)
            rec.all_to_invoice = invoice
