# -*- coding: utf-8 -*-
###################################################################################
#
#
#
###################################################################################
{
    'name': 'Beauty Spa Management',
    'summary': 'Beauty Parlour Management with Online Booking System',
    'version': '15.0.1.0.1',
    'author': 'Nexcel Computer Solution',
    'website': "https://nexcelbahrain.com/",
    'company': 'Nexcel Computer Solutions',
    'maintainer': 'Nexcel Computer Solutions',
    'live_test_url':
        ,
    "category": "Industries",
    'depends': ['account', 'base', 'base_setup', 'mail', 'website'],
    'data': [
             'security/salon_management_groups.xml',
             'security/ir.model.access.csv',
             'data/data.xml',
             'data/mail_template.xml',
             'data/salon_chair_data.xml',
             'data/salon_holiday_data.xml',
             'data/salon_order_data.xml',
             'data/salon_stages_data.xml',
             'data/salon_working_hours_data.xml',
             'views/res_config_settings_views.xml',
             'views/res_partner_views.xml',
             'views/salon_booking_templates.xml',
             'views/salon_booking_views.xml',
             'views/salon_order_views.xml',
             'views/salon_management_views.xml',
             'views/salon_management_menus.xml',
             ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'salon_management/static/src/css/salon_dashboard.css',
            'salon_management/static/src/less/salon_dashboard.less',
        ],
        'web.assets_frontend': [
            'salon_management/static/src/css/salon_website.css',
            'salon_management/static/src/js/website_salon_booking.js',
        ],
    },
}
