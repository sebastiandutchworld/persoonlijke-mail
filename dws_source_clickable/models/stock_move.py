# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
import json


class StockMove(models.Model):
    _inherit = "stock.move"

    def get_html_documents(self, origin_list):
        order_links = []
        models = ['sale.order', 'mrp.production', 'stock.warehouse.orderpoint', 'purchase.order']
        for rec in origin_list:
            for model in models:
                o_id = self.env[model].sudo().search([('name', '=', rec)])
                if o_id:
                    order_links.append(o_id)
                    break
        orders = []
        for order_id in order_links:
            click = 1
            rec = self.env[model].search([('id', '=', order_id.id)])
            if not rec:
                click = 0
            orders.append((order_id.id, order_id._name, order_id.name, click))
        return json.dumps(orders)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    order_links = fields.Char(string='Source Document', compute='_compute_orign_link')

    @api.depends('origin')
    def _compute_orign_link(self):
        for order in self:
            if order.origin:
                origin_list = order.origin.split(', ')
                order.order_links = self.env['stock.move'].get_html_documents(origin_list)
            else:
                order.order_links = False

