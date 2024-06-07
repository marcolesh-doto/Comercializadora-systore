from odoo import models, api
import requests
import logging

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def write(self, vals):
        res = super(StockPicking, self).write(vals)
        _logger.debug("write method called with vals: %s", vals)
        if 'state' in vals and vals['state'] == 'assigned':
            for picking in self:
                _logger.debug("State changed to assigned for picking: %s", picking.name)
                self._trigger_endpoint(picking, 'assigned')
        return res

    def _trigger_endpoint(self, picking, state):
        endpoint_url = 'https://odoo.doto.com.mx/api/v1/vtex/invoice/order'
        headers = {
            'Content-Type': 'application/json',
            'mkp': 'doto'
        }
        sale_order = picking.sale_id  # obtener la orden de venta asociada
        data = {
            'picking_id': picking.id,
            'state': state,
            'order_id': sale_order.id if sale_order else None,
        }
        _logger.debug("Sending data to endpoint: %s", data)
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            _logger.info('Successfully triggered endpoint for stock picking %s', picking.name)
        except requests.exceptions.RequestException as e:
            _logger.error('Failed to trigger endpoint for stock picking %s: %s', picking.name, str(e))