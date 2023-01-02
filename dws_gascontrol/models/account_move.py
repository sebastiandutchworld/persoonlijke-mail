# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.tools.misc import formatLang, format_date, get_lang

class AccountMoveCustom(models.Model):
    _inherit = 'account.move'

    @api.depends('name', 'state')
    def name_get(self):
        result = []
        for move in self:
            if self._context.get('name_groupby'):
                name = '**%s**, %s' % (format_date(self.env, move.date), move._get_move_display_name())
                # if move.ref:
                #     name += '     (%s)' % move.ref
                if move.partner_id.name:
                    name += ' - %s' % move.partner_id.name
            else:
                name = move._get_move_display_name(show_ref=False)
            result.append((move.id, name))
        return result

    def post(self):
        res = super(AccountMoveCustom, self).post()
        for move in self:
            if not move.partner_id: continue
            if move.move_type.startswith('out_'):
                if move.partner_id.parent_id:
                    move.partner_id.parent_id._increase_rank('customer_rank')
            # elif move.type.startswith('in_'):
            #     move.partner_id._increase_rank('supplier_rank')
            else:
                continue
        return res