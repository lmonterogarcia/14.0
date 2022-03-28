from odoo import _, api, fields, models

class HelpdeskTicket(models.Model):
    _inherit = ['helpdesk.ticket']
    
    sale_id = fields.Many2one(string='Orden de venta', comodel_name='sale.order')