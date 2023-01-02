# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields


class ProductPproduct(models.Model):
    _inherit = "product.product"

    description_purchase = fields.Text(
        "Purchase Description", translate=True,
        help="A description of the Product that you want to communicate to your customers. "
             "This description will be copied to every Sales Order, Delivery Order and Customer Invoice/Credit Note")
    description_sale = fields.Text(
        "Sale Description", translate=True,
        help="A description of the Product that you want to communicate to your customers. "
             "This description will be copied to every Sales Order, Delivery Order and Customer Invoice/Credit Note")

    description_picking = fields.Text("Description for Internal Transfers", translate=True)
    description_pickingout = fields.Text(
        "Description for Delivery Orders", translate=True)
    description_pickingin = fields.Text(
        "Description for Receipts", translate=True)
