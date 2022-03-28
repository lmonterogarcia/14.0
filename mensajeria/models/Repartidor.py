# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Repartidor(models.Model):
    _name = 'mensajeria.repartidor'
    _description = 'Delivery Man Class'

    name = fields.Char('Nombre', size=20, required=True)
    last_name = fields.Char('Apellidos', size=80, required=True)
    nif = fields.Char('DNI', size = 9, required=True)
    zona = fields.Selection([('sur', 'Sur'), 
                             ('oeste', 'Oeste'), 
                             ('norte', 'Norte'), 
                             ('este', 'Este')], 
                            'Zona', required=True)
    centro_id = fields.Many2one('mensajeria.centro', string='Centro de reparto', required=True)
    envio_ids = fields.One2many('mensajeria.envio','repartidor_id', 'Envios asignados')
    