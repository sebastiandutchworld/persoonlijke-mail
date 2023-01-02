# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    order_links = fields.Char(string='Source Document', compute='_compute_orign_link')

    @api.depends('origin')
    def _compute_orign_link(self):
        for order in self:
            if order.origin:
                origin_list = order.origin.split(', ')
                order.order_links = self.env['stock.move'].get_html_documents(origin_list)
            else:
                order.order_links = False
