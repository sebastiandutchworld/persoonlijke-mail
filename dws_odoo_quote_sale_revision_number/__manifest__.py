# -*- coding: utf-8 -*-

# noinspection PyStatementEffect
{
    'name': "Sales Quote Revision Numbering and Revision History",
    'version': '1.0',
    'summary': """This module allow you to generate revision of your quotation and revision history.""",
    'description': """

    """,
    'author': "Dutchworld IT Solutions",
    'images': ['static/description/img1.png'],
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