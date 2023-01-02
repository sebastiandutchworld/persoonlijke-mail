# -*- coding: utf-8 -*-
#
# COPYRIGHT
#    Copyright (C) 2020 Dutchworld Solutions

# noinspection PyStatementEffect
{
    'name': 'DWS gascontrol xml invoicing',
    'summary': '''
        This module automatically attaches ubl invoices to emails.''',
    'version': '1.0.0',
    'author': 'Dutchworld Solutions',
    'license': '',
    'depends': ["base",
                'mail',
                'account',                
                "account_einvoice_generate",
                "account_payment_partner",  
                "base_ubl_payment",
                "account_tax_unece"
                ],
    'data': [
        
    ],
    'installable': True,
}
