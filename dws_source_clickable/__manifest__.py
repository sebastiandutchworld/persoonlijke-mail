# -*- coding: utf-8 -*-

{
    'name' : 'Source Clickable',
    'version' : '1.0',
    'category': 'Inventory',
    "author": "Preciseways",
    'website': "www.preciseways.com",
    'summary': 'Source document Clickable in Sale, Purchase, MRP, Stock',
    'sequence': 1,
    'description': """Source Document Clickable""",
    'category': 'warehouse',
    'depends' : ['sale_management', 'purchase', 'stock', 'mrp'],
    'data': [
        'views/stock_move.xml',
        'views/take_from_stock_templates.xml',
    ],
    'installable': True,
    'application': False,
    'images':['static/description/banner.jpg'],
    'license': 'OPL-1',
    'price': '20',
}   
