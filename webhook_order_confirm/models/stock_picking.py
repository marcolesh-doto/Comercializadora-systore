from odoo import models, fields, api
import requests
import logging

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_id = fields.Many2one('sale.order', string='Sale Order', readonly=True)

    @api.model
    def create(self, vals):
        res = super(StockPicking, self).create(vals)
        if vals.get('state') == 'assigned':
            self._trigger_endpoint(res, 'assigned')
        return res

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
        if sale_order:
            data = {
                'state': state,
                'order_id': sale_order.id,
            }

            try:
                response = requests.post(endpoint_url, json=data, headers=headers)
                if response.status_code == 200:
                    _logger.info('Successfully triggered endpoint for stock picking %s', picking.name)
                else:
                    _logger.error('Failed to trigger endpoint for stock picking %s, response: %s', picking.name, response.text)
            except Exception as e:
                _logger.error('Exception occurred when triggering endpoint for stock picking %s: %s', picking.name, str(e))
        else:
            _logger.error('No sale order found for stock picking %s', picking.name)