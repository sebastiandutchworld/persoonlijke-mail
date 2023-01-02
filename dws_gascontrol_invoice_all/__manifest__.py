# -*- coding: utf-8 -*-
#
# COPYRIGHT
#    Copyright (C) 2020 Dutchworld Solutions

# noinspection PyStatementEffect
{
    'name': 'DWS Gascontrol - Invoice All',
    'summary': '''
        This module modifies Odoo to the needs of Gascontrol.''',
    'version': '1.0.0',
    'author': 'Dutchworld Solutions',
    'license': '',
    'depends': [
        'base',
        'sale'
    ],
    'data': [
        'views/sale_order_views.xml'
    ],
    'installable': True,
}
