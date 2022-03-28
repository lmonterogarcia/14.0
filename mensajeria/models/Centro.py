# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Centro(models.Model):
    _name = 'mensajeria.centro'
    _description = 'Client Class'

    name = fields.Char('Nombre', size = 60, required=True)
    center_id = fields.Integer('Codigo del centro', size = 18)
    address = fields.Text('Dirección')
    envio_ids = fields.One2many('mensajeria.envio','cliente_id', 'Envios')
    repartidor_ids = fields.One2many('mensajeria.repartidor', 'centro_id', string='Repartidores')
