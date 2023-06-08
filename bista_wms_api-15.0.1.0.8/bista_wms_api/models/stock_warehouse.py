from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ResUsers(models.Model):
    _inherit = "res.users"

    warehouse_id = fields.Many2one("stock.warehouse", string="Allowed Warehouse")

    def write(self, vals):
        if 'warehouse_id' in vals:
            if self.warehouse_id.id != vals['warehouse_id']:
                assigned_picking = self.env['stock.picking'].search(
                    [('user_id', '=', self.id), ('state', 'not in', ['done', 'cancel']),
                     ('picking_type_id.warehouse_id', '=', self.warehouse_id.id)])
                assigned_batch_picking = self.env['stock.picking.batch'].search(
                    [('user_id', '=', self.id), ('state', 'not in', ['done', 'cancel']),
                     ('picking_type_id.warehouse_id', '=', self.warehouse_id.id)])

                if assigned_picking or assigned_batch_picking:
                    raise ValidationError(_("This user is already assigned to Transfer(s) that are in Ready state. "
                                            "Please remove this user from those Transfer(s) & try again."))
        return super(ResUsers, self).write(vals)

    def action_show_transfer(self):
        self.ensure_one()
        ctx = self._context
        if 'batch_transfer' in ctx and ctx['batch_transfer'] == 1:
            name = _('Batch Transfers')
            res_model = 'stock.picking.batch'
        else:
            name = _('Transfers')
            res_model = 'stock.picking'
        return {
            'name': name,
            'view_mode': 'tree,form',
            'res_model': res_model,
            'type': 'ir.actions.act_window',
            'context': {'create': False, 'delete': False},
            'domain': [('state', 'not in', ['done', 'cancel']), ('user_id', '=', self.id)],
            'target': 'current',
        }


class StockPicking(models.Model):
    _inherit = "stock.picking"

    user_id = fields.Many2one(default=False)
    warehouse_id = fields.Many2one(related='picking_type_id.warehouse_id')

    @api.onchange('picking_type_id')
    def onchange_picking_type_id(self):
        domain = [('groups_id', 'in', self.env.ref('stock.group_stock_user').id), ('share', '=', False)]
        if self.picking_type_id:
            warehouse_id = self.picking_type_id.warehouse_id
            return {'domain': {'user_id': domain + [('warehouse_id', '=', warehouse_id.id)]}}
        else:
            return {'domain': {'user_id': domain}}


class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    warehouse_id = fields.Many2one(related='picking_type_id.warehouse_id')

    @api.onchange('picking_type_id')
    def onchange_picking_type_id(self):
        domain = [('groups_id', 'in', self.env.ref('stock.group_stock_user').id), ('share', '=', False)]
        if self.picking_type_id:
            warehouse_id = self.picking_type_id.warehouse_id
            return {'domain': {'user_id': domain + [('warehouse_id', '=', warehouse_id.id)]}}
        else:
            return {'domain': {'user_id': domain}}
        
        
        
class StockQuantPackages(models.Model):
    _inherit = 'stock.quant.package'
    
    @api.model
    def default_package_sequence(self):
        if self.env.context.get('offline'):
            return self.env['ir.sequence'].next_by_code('stock.quant.packages')
        else:
            return self.env['ir.sequence'].next_by_code('stock.quant.package') or _('Unknown Pack')
    
    name = fields.Char(default=default_package_sequence)
    
    
class Sequence(models.Model):
    _inherit = 'ir.sequence'
    
    is_mobile_app = fields.Boolean(string = 'Mobile App')
    
