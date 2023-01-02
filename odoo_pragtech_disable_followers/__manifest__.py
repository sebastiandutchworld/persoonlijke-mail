{
    'name': 'Odoo Disable Followers',
    'version': '14.0',
    'author': 'Pragmatic TechSoft Pvt Ltd.',
    'website': 'https://www.pragtech.co.in',
    'category': 'mail',
    'summary': 'Odoo Disable Followers add remove mail followers',
    'description': """
Odoo Disable Followers
======================
Add configuration in general setting,add mail followers depends on it.    
""",
    'depends': ['mail'],
    'data': [
        'views/res_config_settings_view.xml'
    ],
    'images': ['images/disable_followers_banner.gif'],
    'live_test_url': 'http://www.pragtech.co.in/company/proposal-form.html?id=103&name=disable-followers',
    'currency': 'USD',
    'price': 29,
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False,
    'active': False,

}
