# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import timedelta


class purchase_order_wizard(models.TransientModel):
	_name = 'purchaseorder.wiz'
	_description = "purchase order wizard"

	partner_id = fields.Many2one('res.partner', string='Vendor')
	scheduled_date = fields.Datetime(string='Scheduled Date')
	purchase_order_ids = fields.One2many('purchase_wiz', 'sale_wiz_id',string='purchase order Create')

	partner_ids = fields.Many2many('res.partner')
	supplier_warning = fields.Boolean(default=False)

	# set so lines in wizard view
	@api.model
	def default_get(self, vals):
		print('default get')
		terns_obj = self.env['sale.order'].browse(self._context.get('active_ids'))

		# collect product ids in purchase orders
		po_ids = self.env['purchase.order'].search([('sale_ord_id', '=', self._context.get('active_id'))])
		product_ids = self.env['purchase.order.line'].search([('order_id', 'in', po_ids.ids)]).mapped('product_id')
		partner_ids = terns_obj.mapped('order_line') \
			.filtered(lambda l: l.product_id not in product_ids) \
			.filtered(lambda k: 'Buy' in k.with_context(lang='en_US').product_id.route_ids.mapped('name')) \
			.mapped('product_id').mapped('seller_ids').mapped('name').mapped('id')
		# print('partner_ids', partner_ids)
		supplier_warning = False

		if not terns_obj.order_line:
			raise UserError(_("Please add some valid sale order lines...!"))
		else:
			for rec in terns_obj.order_line:
				if not rec.product_id.seller_ids \
						and not rec.display_type == 'line_section' \
						and 'Buy' in rec.with_context(lang='en_US').product_id.route_ids.mapped('name') \
						and rec.product_id.purchase_ok == True:
					# check also if route_id with name is 'Buy' is present
					# raise UserError(_("Product " + (rec.product_id.name or '') + " has no supplier"))
					supplier_warning = True
		res = super(purchase_order_wizard, self).default_get(vals)
		res.update(
			{'purchase_order_ids': [], 'partner_ids': [(6, 0, partner_ids)], 'supplier_warning': supplier_warning})
		return res

	@api.onchange("partner_id")
	def _calc_price(self):
		print('onchange partner id')
		for rec in self.purchase_order_ids:
			self.purchase_order_ids = [(2, rec.id)]
		terns = []
		active_ids = self._context.get('active_ids')
		# print('active ids', active_ids)
		terns_obj = self.env['sale.order'].browse(active_ids)
		# collect product ids in purchase orders
		po_ids = self.env['purchase.order'].search([('sale_ord_id', '=', self._context.get('active_id'))])
		product_ids = self.env['purchase.order.line'].search([('order_id', 'in', po_ids.ids)]).mapped('product_id')
		for rec in terns_obj.order_line:
			# print('rec', rec)
			if rec.product_id.id not in product_ids.ids and 'Buy' in rec.with_context(
					lang='en_US').product_id.route_ids.mapped('name'):
				for seller_id in rec.product_id.seller_ids:
					# print('seller_id', seller_id)
					if seller_id.name.id == self.partner_id.id:
						# filter out product var
						if seller_id.product_id.id:
							if rec.product_id.id != seller_id.product_id.id:
								continue
						terns.append((0, 0, {
							'product_id': rec.product_id.id,
							'description': rec.name,
							'product_uom_qty': rec.product_uom_qty,
							'price_unit': seller_id.price,
							'product_uom': rec.product_uom.id,
							'price_subtotal': rec.price_subtotal,
						}))
		self.purchase_order_ids = terns

	def create_po(self):
		po_object = self.env['purchase.order']
		result = []
		active_ids = self._context.get('active_ids')
		so_obj = self.env['sale.order'].browse(active_ids)

		now = fields.Datetime.now()
		now_5_date = now - timedelta(minutes=1)

		if self.scheduled_date:
			if self.scheduled_date < now_5_date:
				raise UserError(_("Please enter valid scheduled date...!"))
		for line in self.purchase_order_ids:
			result.append((0, 0, {'product_id': line.product_id.id,
								  'name': '',
								  # line.product_id.with_context(lang=self.partner_id.lang, partner_id=self.partner_id.id, company=self.env.company).display_name,
								  'product_qty': line.product_uom_qty,
								  'date_planned': self.scheduled_date,
								  'product_uom': line.product_uom.id,
								  'price_unit': line.price_unit,
								  'price_subtotal': line.price_subtotal,
								  }))
		po_order = po_object.create({'partner_id': self.partner_id.id,
									 'order_line': result,
									 'origin': so_obj.name,
									 'payment_term_id': self.partner_id.property_supplier_payment_term_id.id,
									 'date_planned': self.scheduled_date,
									 'fiscal_position_id': self.partner_id.property_account_position_id.id,
									 'sale_ord_id': so_obj.id})
		for po_line in po_order.order_line:
			po_line._product_id_change()
		context = dict(self.env.context or {})
		return {
			'name': _('Purchase Order'),
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'purchase.order',
			'view_id': self.env.ref('purchase.purchase_order_form').id,
			'res_id': po_order.id,
			'type': 'ir.actions.act_window',
			'target': 'self',
		}

class purchase_wiz(models.TransientModel):
	_name = 'purchase_wiz'
	_description = "purchase wizard lines"

	sale_wiz_id = fields.Many2one('purchaseorder.wiz')
	product_id = fields.Many2one('product.product',string='Product')
	product_uom = fields.Many2one('uom.uom')
	description = fields.Char(string='Description')
	product_uom_qty = fields.Float(string='Quantity')
	price_unit = fields.Float(string='Price unit')
	price_subtotal = fields.Float(string='Price Subtotal')

	sale_ord_id = fields.Many2one('sale.order', string='Sale Order',readonly=True, copy=False)