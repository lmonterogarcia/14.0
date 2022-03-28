
# -*- coding: utf-8 -*-
from odoo import models, fields, api

class megamarket(models.Model):
    _name = 'megamarket.cliente'
    _description = 'Cliente de Megamarket'
     
    name = fields.Char('Nombre', required=True)
    surname = fields.Char('Apellidos', required=True)
    nif = fields.Char('DNI', required=True)
    address = fields.Text('Dirección')
    birth_date = fields.Date('Fecha de nacimiento', autodate = True)
    telephone = fields.Integer('Teléfono')
