# Copyright © 2021 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# @author: Iryna Razumovska (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from odoo import fields, models



class PrintProductLabel(models.TransientModel):
    _inherit = "print.product.label"

    template = fields.Selection(
        selection_add=[(
            'garazd_product_label_38x25.report_product_label_38x25',
            'Label 38x25 mm (1.5" x 1")'
        )],
        default='garazd_product_label_38x25.report_product_label_38x25',
    )

