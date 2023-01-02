# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleCustomContacts(models.Model):
    _inherit = 'sale.order'

    contact_person = fields.Many2many('res.partner')
    purchase_contact = fields.Many2one('res.partner')
