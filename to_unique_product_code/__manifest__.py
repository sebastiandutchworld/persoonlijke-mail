{
    'name': "Unique Product Code",
    'name_vi_VN':"Mã Sản Phẩm không trùng lặp",

    'summary': """
Unique Product Default Code""",
    'summary_vi_VN': """
Ngăn nhập mã mặc định của Sản Phẩm trùng lặp""",

    'description': """
This module, once installed, will block saving and raise an error message when users try to input a code (also known as "Internal Reference")
that is currently used by another product.

Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,
    'description_vi_VN': """
Khi module này được cài đặt, sẽ không cho lưu và hiện thông báo lỗi khi người dùng nhập mã (hay còn gọi là "Tham chiếu nội bộ")
đang được sản phẩm khác sử dụng.

Ấn bản hỗ trợ
==============
1. Ấn bản cộng đồng
2. Ấn bản doanh nghiệp

    """,

    'author': "T.V.T Marine Automation (aka TVTMA)",
    'website': 'https://www.tvtmarine.com',
    'live_test_url': 'https://v13demo-int.erponline.vn',
    'support': 'support@ma.tvtmarine.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 9.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}