# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Picking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def take_from_stock(self):
        for move_line in self.move_lines:
            move_line.write({'procure_method':'make_to_stock'})
            for move_orig_id in move_line.move_orig_ids:
                move_line.write({'move_orig_ids': [(3, move_orig_id.id, None)]})