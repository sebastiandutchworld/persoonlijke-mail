# -*- coding: utf-8 -*-

{
    'name' : 'Sale MRP Status',
    'author': "Edge Technologies",
    'version' : '13.0.1.0',
    'live_test_url':'https://youtu.be/_BpUsZicITw',
    "images":["static/description/main_screenshot.png"],
    'summary' : 'manufacturing status in sales order manufacturing status in SO MRP status in Sales order production status on sales order manufacturing order status in sales order view MO status in SO MO status in sales order',
    'description' : """
        This module is useful for see the manufacturing status in sales order.
    """,
	'depends' : ['base','sale_management','mrp'],
    "license" : "OPL-1",
	'data' : [
		'views/so_to_manufacturing_status.xml',	
	],
    'qweb' : [],
    'demo' : [],
    'installable' : True,
    'auto_install' : False,
    'price': 7,
    'currency': "EUR",
    'category' : 'Sales',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
