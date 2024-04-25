# -*- coding: utf-8 -*-
{
    'name': 'Stock Picking Barcode',
    'summary': """
        This modules support for barcodes scanning to Stock Picking.
    """,
    'description': """
        This modules support for barcodes scanning to the Inventory Management & will help you in pickings to make your process faster.
    """,
    'author': 'Do Incredible',
    'website': 'http://doincredible.com',
    'license': 'OPL-1',
    'category': 'Warehouse',
    'sequence': '10',
    'version': '1.0.0',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'do_stock_barcode/static/src/css/custom.css',
            'do_stock_barcode/static/src/js/barcode.js',
        ],
    },
    'images': ['static/description/logo.jpg'],
    'application': True,
    'price': 15,
    'currency': 'EUR',
    'live_test_url': 'https://youtu.be/_lDXS6k6VNQ',
}
