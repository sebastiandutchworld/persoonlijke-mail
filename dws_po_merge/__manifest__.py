# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'DWS Purchase Order Merge',
    'version': '14.0.0.0',
    'category': 'Purchase',
    'summary': 'Merge sale order merge sales order merge purchase order merge multiple sales order merge multiple purchase order merge mass sales order merge mass purchase order merger sale merger purchase merge Delivery order merge picking merge SO merge PO',
    'description': """
    Merge sales order, merge purchase orders, merge order, merge data,
    Sales Order Merge,
    Purchase Order Merge, Merge Sale Order, Merge purchases Order
    purchase order merger
    purchases order merger
    merger purchase order
    merge request for quotation
    request for quotation merger
    merge request of quotation orders
""",
    'author': 'BrowseInfo',
    'website': 'https://www.browseinfo.in',
    "price": 19,
    "currency": 'EUR',
    'depends': ['base','purchase','product'],
    'data': ['security/ir.model.access.csv',
        'views/order_merge_view.xml',
        'views/purchase_order.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    "live_test_url":'https://youtu.be/F2AolIRpTuQ',
    "images":["static/description/Banner.png"],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
