# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductSupplierinfoCustom(models.Model):
    _inherit = 'product.supplierinfo'

    product_is_active = fields.Boolean("Product is active", compute='_compute_product_is_archived', store=True)

    #compute entire list view when opening the product.supplierinfo list view
    @api.depends('product_tmpl_id.active')
    def _compute_product_is_archived(self):
        for record in self:
            record.product_is_active = record.product_tmpl_id.active


    #
        


