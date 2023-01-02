# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PartnerCustom(models.Model):
    _inherit = 'res.partner'

    extra = fields.Char('')