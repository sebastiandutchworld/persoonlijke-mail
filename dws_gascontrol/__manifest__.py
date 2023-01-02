# -*- coding: utf-8 -*-
#
# COPYRIGHT
#    Copyright (C) 2020 Dutchworld Solutions

# noinspection PyStatementEffect
{
    'name': 'DWS Gascontrol',
    'summary': '''
        This module modifies Odoo to the needs of Gascontrol.''',
    'version': '1.0.0',
    'author': 'Dutchworld Solutions',
    'license': '',
    'depends': [
        'base',
        'sale',
        'sale_crm',
        'account',
        'product',
        'purchase'
    ],
    'data': [
        'data/mail_template_data_custom.xml',
        'data/ir_cron.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/product_views.xml',
        'views/report_sale.xml',
        'views/report_stock.xml',
        'views/report_stock_internal.xml',
        'views/report_purchase_order.xml',
        'views/report_purchase_quotation.xml',
        # 'views/mail.xml',
        'views/template.xml',
        'views/stock_picking_views.xml',
        'views/vendor_pricelist.xml'
    ],
    'installable': True,
}
