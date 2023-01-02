# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CronCustom(models.Model):
    _name = 'dws.gascontrol.cron'

    def create_reordering_rules(self):
        # for all products with route 'buy' create a reordering rule if there is none
        print("cron reordering rules")
        products = self.env['product.product'].search([])
        for product in products:
            for route_id in product.route_ids:
                if route_id.id == 5:
                    # print("route id is buy")
                    # then create reordering rule if there is none
                    reorder_rule = self.env['stock.warehouse.orderpoint'].search([('product_id', '=', product.id)], limit=1)
                    if not reorder_rule:
                        # create reorder rule
                        new_reorder_rule = self.env['stock.warehouse.orderpoint'].create({
                            'product_id': product.id,
                            'product_min_qty': 0,
                            'product_max_qty': 0,
                        })
                        print("created new reorder rule:", new_reorder_rule.name)
                        break