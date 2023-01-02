# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseCustom(models.Model):
    _inherit = 'purchase.order'

    delivery_date = fields.Datetime(compute='_compute_delivery_date')

    @api.depends('name', 'partner_ref')
    def name_get(self):
        result = []
        for po in self:
            name = po.name
            # if po.partner_ref:
            #     name += ' (' + po.partner_ref + ')'
            # if self.env.context.get('show_total_amount') and po.amount_total:
            #     name += ': ' + formatLang(self.env, po.amount_total, currency_obj=po.currency_id)
            result.append((po.id, name))
        return result