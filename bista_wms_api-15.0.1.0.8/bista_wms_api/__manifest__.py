# -*- coding: utf-8 -*-
{
    'name': "Bista WMS API",

    'summary': """APIs for WMS mobile app.""",

    'description': """
        This module includes the following features:
            - Customized Login API endpoint
            - 
    """,

    'author': "Bista Solutions Pvt. Ltd.",
    'website': "https://www.bistasolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '15.0.1.0.8',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'product',
        'stock',
        'sale',
        'sale_stock',
        'purchase',
        'purchase_stock',
        'stock_picking_batch',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'data/data.xml',
        'data/ir_sequence.xml',
        "views/res_users.xml",
        "views/stock_picking.xml",
        'views/res_config_settings_views.xml',
    ],
    'images': ['static/description/images/banner.gif'],
}
