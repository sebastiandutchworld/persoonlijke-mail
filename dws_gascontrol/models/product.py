# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplateCustom(models.Model):
    _inherit = 'product.template'

    url = fields.Char('')

class ProductCustom(models.Model):
    _inherit = 'product.product'

    def get_product_multiline_description_sale(self):
        """ Compute a multiline description of this product, in the context of sales
                (do not use for purchases or other display reasons that don't intend to use "description_sale").
            It will often be used as the default description of a sale order line referencing this product.
        """
        name = self.display_name
        if self.description_sale:
            name += '\n' + self.description_sale
        elif self.product_tmpl_id and self.product_tmpl_id.description_sale:
            name += '\n' + self.product_tmpl_id.description_sale

        return name