# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente(models.Model):
    _name = 'mensajeria.cliente'
    _description = 'Client Class'

    name = fields.Char('Nombre', size=20, required=True)
    last_name = fields.Char('Apellidos', size=80, required=True)
    nif = fields.Char('DNI', size = 9, required=True)
    address = fields.Text('Dirección')
    envio_ids = fields.One2many('mensajeria.envio','cliente_id', 'Envios')
