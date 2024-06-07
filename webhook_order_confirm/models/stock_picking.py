from odoo import models, api
import requests
import logging

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def write(self, vals):
        res = super(StockPicking, self).write(vals)
        if 'state' in vals and vals['state'] == 'assigned':
            for picking in self:
                self._trigger_endpoint(picking, 'assigned')
        return res

    def _trigger_endpoint(self, picking, state):
        endpoint_url = 'https://odoo.doto.com.mx/api/v1/vtex/invoice/order'
        headers = {
            'Content-Type': 'application/json',
            'mkp': 'doto'
        }
        sale_order = picking.sale_id
        data = {
            'picking_id': picking.id,
            'state': state,
            'order_id': sale_order.id if sale_order else None,
        }
        response = requests.post(endpoint_url, json=data, headers=headers)
        if response.status_code != 200:
            _logger.error(
                'Failed to trigger endpoint for stock picking %s', picking.name)