# Copyright © 2021 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# @author: Iryna Razumovska (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'Custom Product Labels 38x25 mm (1.5" x 1")',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'license': 'LGPL-3',
    'summary': 'Print custom product barcode labels 38x25 mm (1.5 x 1.0 inches)',
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'live_test_url': 'https://apps.garazd.biz/r/j8D',
    'depends': [
        'garazd_product_label',
    ],
    'data': [
        'report/product_label_reports.xml',
        'report/product_label_templates.xml',
    ],
    'external_dependencies': {
    },
    'support': 'support@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
