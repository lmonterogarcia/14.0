# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Pago(models.Model): 
    _name = 'gym.pago' 
    _description = 'Pagos Classes'

    id_pago = fields.Integer('Código', required=True)
    concept = fields.Char('Concepto', size = 60, required=True, help = "Concepto del pago")
    amount = fields.Float('Cuantía', (4,2), required=True)
    user_ids = fields.Many2one('gym.users', 'Usuario', required=True)
    payment_date = fields.Date('Fecha de pago', required=True)
    
    @api.constrains("id_pago")
    def _check_id_pago(self):
        for record in self:
            if len(record.id_pago) > 10:
                raise ValidationError(_("El 'Código' solo puede tener hasta 10 números"))