{
    "name": "Product All Pricelist || Product Pricelist Listview",
    "version": "14.1.1.1",
    "description": """
        Using this module you can display all price list apply on the product with amount in form view and list view.
    """,
    'price': 20,
    'currency': 'EUR',
    "author" : "MAISOLUTIONSLLC",
    'sequence': 1,
    "email": 'apps@maisolutionsllc.com',
    "website":'http://maisolutionsllc.com/',
    'license': 'OPL-1',
    'category':"Sales",
    'summary':"Using this module you can display all price list apply on the product with amount in form view and list view.",
    "depends": [
        "sale_management",
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/product_view.xml',
    ],
    'qweb': [],
    'css': [],
    'js': [],
    "images": ['static/description/main_screenshot.png'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
