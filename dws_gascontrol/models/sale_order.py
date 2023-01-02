# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleCustom(models.Model):
    _inherit = 'sale.order'

    internal_reference = fields.Char('')
    tag_ids = fields.Many2many(related='opportunity_id.tag_ids', string='Tags')
