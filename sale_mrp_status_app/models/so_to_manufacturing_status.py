# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class SaleOrder(models.Model):
	_inherit = 'sale.order'

	custom_mrp_count = fields.Integer('Manufacturing', compute="_compute_custom_mrp_count")
	mrp_state = fields.Char(compute="_compute_custome_state_mrp", string='MRP')

	def _compute_custom_mrp_count(self):
		for so_obj in self:
			mrp = self.env['mrp.production'].search_count([('origin','=', so_obj.name)])
			so_obj.custom_mrp_count = mrp

	def action_view_custom_mrp(self):
		action = self.env.ref('sale.view_order_tree').read()[0]
		sale_mrp = self.env['mrp.production'].search([('origin','=', self.name)])
		return {
			'name': _('Manufacturing Order'),
			'view_mode': 'tree,form',
			'res_model': 'mrp.production',
			'domain': [('id', 'in', sale_mrp.ids)],
			'type': 'ir.actions.act_window',
			}

	def _compute_custome_state_mrp(self):
		for so_obj in self:
			mrp = self.env['mrp.production'].search([('origin','=', so_obj.name)],limit=1)
			if mrp.state == 'progress':
				so_obj.mrp_state = 'In Progress'
			elif mrp.state == 'confirmed':
				so_obj.mrp_state = 'Confirmed'
			elif mrp.state == 'done':
				so_obj.mrp_state = 'Done'
			elif mrp.state == 'cancel':
				so_obj.mrp_state = 'Cancelled'
			elif mrp.state == 'planned':
				so_obj.mrp_state = 'Planned'	
			else:
				so_obj.mrp_state = mrp.state
