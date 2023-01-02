# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': "DWS Universal Discount",
    'summary': """
        DWS Universal Discount""",
    'description': """

CHANGELOG:

- #976 date 2021 07 09 add check different tax rate at order confirmation
    """,
    'author': "DWS",
    'website': "https://www.dutchworld.nl",
    'category': 'Sales Management',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'depends': ['base', 'sale', 'purchase', 'account', 'sale_management', 'sale_margin'],
    'data': [
        'views/ks_sale_order.xml',
        'views/ks_account_invoice.xml',
        'views/ks_purchase_order.xml',
        'views/ks_account_invoice_supplier_form.xml',
        'views/ks_account_account.xml',
        'views/ks_report.xml'
    ],

}
