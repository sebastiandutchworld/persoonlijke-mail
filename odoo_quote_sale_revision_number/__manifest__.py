# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': "Sales Quote Revision Numbering and Revision History",
    'version': '2.1',
    'price': 49.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'summary': """This module allow you to generate revision of your quotation and revision history.""",
    'description': """
    Odoo Quote Sale Revision Number
    This module provide functionality that keep old Quote/Sale order History
    
    This module provide functionality that keep old Quote History
    This module provide functionality that keep old Sale History
    Quote History
    Sale History
Odoo Sales Quote Revision
odoo sale quote revision
odoo quote revisions
odoo quote revision
quotation revision
sale quotation revision
quotation order quotation
customer quotation revision
order quotation revision
quote revision odoo
customer quote revision odoo
odoo revision quotes
sales revision
quote revision
sale order revision
sale quote revision
order revision
customer quote revision
sales order and quote revision
revision quote
quote customer revision
revision history
revised history
revision quote
revised quote
quote revised
order revised
sale order revised

    """,
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "http://www.probuse.com",
    'support': 'contact@probuse.com',
    'images': ['static/description/img1.png'],
    'live_test_url' : 'https://youtu.be/PQRDAy7zRBY',
    'category' : 'Sales',
    'depends': [
                'sale',
                ],
    'data':[
        'security/ir.model.access.csv',
        'security/revision_security.xml',
        'views/sale_view.xml',
        'views/revisedline_view.xml',
        'views/saleorder_revised_view.xml',
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
