from odoo import models, api, _
from odoo.exceptions import ValidationError


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.constrains('default_code')
    def constrains_default_code(self):
        for r in self:
            if not r.default_code:
                continue

            domain = [('id', '!=', r.id), ('default_code', '=', r.default_code)]
            overlapping = self.search(domain, limit=1)

            if overlapping:
                raise ValidationError(_('Invalid Code! The code "%s" has been assigned to the product "%s".'
                                        ' Please input another code!')
                                      % (r.default_code, overlapping.display_name))

