# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleCustom(models.Model):
    _inherit = 'stock.picking'

    commitment_date = fields.Datetime()


