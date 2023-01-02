# -*- coding: utf-8 -*-

{
    'name' : 'Create Sale Order to Purchase Order',
    'author': "Edge Technologies",
    'version' : '13.0.1.0',
    'live_test_url':'https://youtu.be/UyuzOP1pVKA',
    'images':["static/description/main_screenshot.png"],
    'summary' : 'This apps help for Convert Sale to purchase create sales to purchase PO from SO to PO quick sale order to purchase quick sales to purchase easy to create sale order from purchase convert sales order from purchase order SO from PO',
    'description' : """
        This app is useful for create and view purchase order from sale order in odoo.
    """,
	'depends' : ['base','sale_management','purchase'],
    "license" : "OPL-1",
	'data' : [
		'security/ir.model.access.csv',
		'wizard/purchase_order_wiz.xml',
		'views/sale_order_to_purchase_order_app.xml',
		
	],
    'qweb' : [],
    'demo' : [],
    'installable' : True,
    'auto_install' : False,
    'price': 12,
    'currency': "EUR",
    'category' : 'Sales',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: