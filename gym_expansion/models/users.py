from odoo import models, fields, api, _

class Users(models.Model):
    _inherit = 'gym.users'

    materiales_ids = fields.Many2many('gym_expansion.materiales' ,string='Materiales usados')