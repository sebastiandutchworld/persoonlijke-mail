# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPickingCustom(models.Model):
    _inherit = 'stock.picking'

    sale_responsible = fields.Many2one('res.users', 'Sale Responsible', related='sale_id.user_id')

    # def button_validate(self):
    #     if (self.picking_type_id.id == 1):
    #         # print('WH/IN confirmed')
    #         self._mail_on_confirm_wh_in()
    #     return super(StockPickingCustom, self).button_validate()

    def _mail_on_confirm_wh_in(self):
        purchase_order = self.env['purchase.order'].search([('picking_ids', 'in', self.id)])
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        # print('purchase order =', purchase_order.name)
        ctx = self.env.context.copy()
        ctx.update({
            'po': purchase_order,
            'base_url': base_url,
        })
        template = self.env.ref('dws_gascontrol.wh_in_confirmed')
        self.env['mail.template'].sudo().browse(template.id).with_context(ctx).send_mail(self.id)
