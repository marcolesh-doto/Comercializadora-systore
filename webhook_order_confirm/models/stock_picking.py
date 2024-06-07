import json
import requests
from odoo import models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        picking = super(StockPicking, self).create(vals)
        if picking.state == 'assigned':
            self._trigger_endpoint(picking, picking.state)
        return picking

    def write(self, vals):
        res = super(StockPicking, self).write(vals)
        for picking in self:
            if 'state' in vals and vals['state'] == 'assigned':
                self._trigger_endpoint(picking, vals['state'])
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
        response = requests.post(endpoint_url, headers=headers, data=json.dumps(data))
        if response.status_code != 200:
            raise UserError('Error sending request to endpoint: {}'.format(response.text))
        return response