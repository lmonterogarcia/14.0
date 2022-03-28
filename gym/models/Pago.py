# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Pago(models.Model): 
    _name = 'gym.pago' 
    _description = 'Pagos Classes'

    id_pago = fields.Integer('Código', size = 10, required=True)
    concept = fields.Char('Concepto', size = 60, required=True, help = "Concepto del pago")
    amount = fields.Float('Cuantía', (4,2), required=True)
    user_ids = fields.Many2one('gym.users', 'Usuario', required=True)
    payment_date = fields.Date('Fecha de pago', required=True)
    