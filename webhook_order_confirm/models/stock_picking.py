from odoo import models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.depends('state')
    def _check_state_and_trigger_endpoint(self):
        for picking in self:
            if picking.state == 'assigned':
                sale_order = picking.sale_id
                if sale_order:
                    sale_order._trigger_endpoint(sale_order, 'assigned')

    state = fields.Selection(track_visibility='onchange', compute='_check_state_and_trigger_endpoint', store=True)

    def write(self, vals):
        res = super(StockPicking, self).write(vals)
        if 'state' in vals and vals['state'] == 'assigned':
            self._check_state_and_trigger_endpoint()
        return res