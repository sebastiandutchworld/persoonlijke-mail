# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    revised_custom_ids = fields.One2many(
        'saleorder.revised',
        'sale_order_id',
        string='Revised',
        copy=False,
    )
    custom_counter = fields.Integer(
        default=0,
        copy=False,
     )
    custom_store_name = fields.Char(
        string="Store value",
         copy=False,
    )
    
#    @api.multi #odoo13
    def custom_create_revision(self):
        for rec in self:
            rec._revised_state_custom()

    @api.model
    def _revised_state_custom(self):
        for rec in self:
            if rec.custom_counter == 0:
                rec.custom_store_name = rec.name
            rec.custom_counter += 1
            revised_vals = {'revised_number': rec.name ,'sale_order_id': rec.id}
            revised_obj = self.env['saleorder.revised'].sudo().create(revised_vals)
            for line in rec.order_line:
                reline_vals = {
                    'product_id_rev': line.product_id.id,
                    # 'layout_category_id_rev' : line.layout_category_id.id, #  'sale.order.line' object has no attribute 'layout_category_id' in odoo12
                    'name_rev' : line.name,
                    'qty_rev' : line.product_uom_qty,
                    'uom_rev' : line.product_uom.id,
                    'price_rev' : line.price_unit,
                    'discount_rev' : line.discount,
                    'subtotal_rev' : line.price_subtotal,
                    'total_rev' : line.price_total,
                    'line_custom_id': revised_obj.id,
                }
                rline = self.env['saleorderline.revised'].sudo().create(reline_vals)
            vals = {
                'name' : rec.custom_store_name + '-R '+ str(rec.custom_counter),
                'state' : 'draft',
                'date_order': fields.Datetime.now(),
                'validity_date': self._default_validity_date()
            }
            rec.write(vals)
        return True
            
#    @api.multi #odoo13
    def show_revisedline(self):
        rline = []
        for rec in self:
            for order in rec.revised_custom_ids:
                for line in order.revised_line_ids:
                    rline.append(line.id)
            res = self.env.ref('odoo_quote_sale_revision_number.action_sale_order_line_revised')
            res = res.read()[0]
            res['domain'] = str([('id','in',rline)])
        return res
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
