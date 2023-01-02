# -*- coding: utf-8 -*-
#
# COPYRIGHT
#    Copyright (C) 2020 Dutchworld Solutions

# noinspection PyStatementEffect
{
    'name': 'DWS Custom',
    'summary': '''
        This module modifies Odoo to the needs of DWS Custom modifications.''',
    'version': '1.0.0',
    'author': 'Dutchworld Solutions',
    'license': '',
    'depends': [
        'base',
        'stock',
        'purchase'
    ],
    'data': [
        'views/res_partner_views.xml',
        'report/report_purchase_order_template_customization.xml',
        'report/report_deliveryslip_customization.xml'
    ],
    'installable': True,
}
