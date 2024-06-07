from odoo import models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def write(self, vals):
        res = super(StockPicking, self).write(vals)
        if 'state' in vals and vals['state'] == 'assigned':
            for picking in self:
                if picking.state == 'assigned':
                    sale_order = picking.sale_id
                    if sale_order:
                        sale_order._trigger_endpoint(sale_order, 'assigned')
        return res