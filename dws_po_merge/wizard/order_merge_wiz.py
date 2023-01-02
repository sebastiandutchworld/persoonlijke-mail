# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError, Warning
import copy

class PurchaseOrderMerge(models.TransientModel):
    _name = 'purchase.order.merge'
    _description = 'Merge Purchase orders'

    @api.model
    def default_get(self, fields):
        rec = super(PurchaseOrderMerge, self).default_get(fields)
        context = dict(self._context or {})
        active_model = context.get('active_model')
        active_ids = context.get('active_ids')
        
        if active_ids:
            purchase_ids = []
            purchases = self.env['purchase.order'].browse(active_ids)
            
            if any(pur.state == 'done' for pur in purchases):
                raise UserError ('You cannot merge orders that are done.')
                    
            purchase_ids = [pur.id for pur in purchases if pur.state in ('draft')]
                 
            if 'order_to_merge' in fields:
                rec.update({'purchase_order_to_merge': purchase_ids})
        return rec

    purchase_order = fields.Many2one(
        'purchase.order', 'Merge into')
    purchase_order_to_merge = fields.Many2many(
        'purchase.order', 'rel_purchase_to_merge', 'purchase_id', 'to_merge_id',
        'Orders to merge')
    type = fields.Selection(
        [('exist_1', 'Merge orders into existing selected order and cancel others'),
         ('exist_2', 'Merge orders into existing selected order and delete others')], 'Merge Type', default='exist_1',
        required=True)

    def merge_purchase(self):
        purchase_obj = self.env['purchase.order']
        mod_obj = self.env['ir.model.data']
        line_obj = self.env['purchase.order.line']
        form_view_id = mod_obj.xmlid_to_res_id('purchase.purchase_order_form')
        purchases = purchase_obj.browse(self._context.get('active_ids', []))
        partners_list = []
        partners_list_write = []
        line_list= []
        cancel_list = []
        copy_list = []
        vendor_ref = []
        myString = ''
        new_purchase = False        
        if len(purchases) < 2:
            raise UserError ('Please select multiple orders to merge in the list view.')
                    
        if any(pur.state in ['done','purchase','cancel'] for pur in purchases):
            raise UserError ('You cannot merge this order with existing state.')
        for pur in purchases:
            if pur.partner_ref:
                vendor_ref.append(pur.partner_ref)
                if len(vendor_ref) > 1:
                    myString = ",".join(vendor_ref)
                else:
                    myString = vendor_ref[0]

        msg_origin = ""
        origin_list = []

        for i in range(len(origin_list)):
            if i == len(origin_list) - 1:
                msg_origin = msg_origin + origin_list[i] + "."
            else :
                msg_origin = msg_origin + origin_list[i] + ","

        for pur in purchases :
            origin_list.append(pur.name)


        if self.purchase_order:
            self.purchase_order.write({'partner_ref':myString})

        if self.type == 'exist_1':
            for pur in purchases:
                partners_list_write.append(pur.partner_id)
                partners_list_write.append(self.purchase_order.partner_id)
                cancel_list.append(pur.id)

                user = partners_list_write
                set1 = set(partners_list_write)
                if len(set1) > 1:
                    raise UserError ('You can only merge orders of same partners.')
                else:
                    partner_name = pur.partner_id.id
                    merge_ids = line_obj.search([('order_id', '=', pur.id)])
                    for line in merge_ids:
                        line.write({'order_id':self.purchase_order.id})

            msg_body = _("This purchases order has been created from: <b>%s</b>") % (msg_origin)
            self.purchase_order.message_post(body=msg_body)

            if self.purchase_order.id in cancel_list:
                cancel_list.remove(self.purchase_order.id)
            for orders in cancel_list:
                for s_order in self.env['purchase.order'].browse(orders):
                    s_order.button_cancel()
            return True

        if self.type == 'exist_2':
            for pur in purchases:
                partners_list_write.append(pur.partner_id)
                partners_list_write.append(self.purchase_order.partner_id)
                cancel_list.append(pur.id)
                
                user = partners_list_write
                set1 = set(partners_list_write)
                if len(set1) > 1:
                    raise UserError ('You can only merge orders of same partners.')
                else:
                    if self.purchase_order.state in ['done','purchase','to approve','cancel']:
                        raise UserError ('You cannot merge orders with Done, Cancel and Purchase order orders.')
                    partner_name = pur.partner_id.id
                    merge_ids = line_obj.search([('order_id', '=', pur.id)])
                    for line in merge_ids:
                        line.write({
                            'order_id':self.purchase_order.id
                        })

            msg_body = _("This purchases order has been created from: <b>%s</b>") % (msg_origin)
            self.purchase_order.message_post(body=msg_body)

            if self.purchase_order.id in cancel_list:
                cancel_list.remove(self.purchase_order.id)
            for orders in cancel_list:
                p_order =self.env['purchase.order'].browse(orders)
                p_order.button_cancel()
                p_order.unlink()
            return True
                
        result =  {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': new_purchase.id,
            'views': [(False, 'form')],
        }
        return result
    
