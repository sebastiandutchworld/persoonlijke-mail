# -*- coding: utf-8 -*-

# noinspection PyStatementEffect
{
    'name' : 'Create Sale Order to Purchase Order',
    'author': "Dutchworld IT Solutions",
    'version' : '13.0.1.0',
    'summary' : "Create Sale Order to Purchase Order",
    'description' : """
    """,
	'depends' : ['base','sale_management','purchase'],
	'data' : [
		'security/ir.model.access.csv',
		'wizard/purchase_order_wiz.xml',
		'views/sale_order_to_purchase_order_app.xml'
	],
    'qweb' : [],
    'demo' : [],
    'installable' : True,
    'auto_install' : False,
    'category' : 'Sales',
}
