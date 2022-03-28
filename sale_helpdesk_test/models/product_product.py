from odoo import _, api, fields, models

class ProductProduct(models.Model):
    _inherit = ['product.product']
    
    helpdesk_tag_id = fields.Many2one(string='Helpdesk tag', comodel_name='helpdesk.ticket.tag')