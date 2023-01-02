# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    internal_reference = fields.Char('')

    def action_confirm(self):
        for order in self:
            if not order.fiscal_position_id:
                raise ValidationError(
                    'Fiscal position must be defined before confirming the order!')
            else:
                if order.fiscal_position_id.vat_required and not order.partner_shipping_id.vat:
                    raise ValidationError('VAT number must be defined for the delivery address of this customer!')

        result = super(SaleOrder, self).action_confirm()
        return result