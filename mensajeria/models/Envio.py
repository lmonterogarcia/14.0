# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Envio(models.Model):
    _name = 'mensajeria.envio'
    _description = 'Delivery Man Class'

    shipping_code = fields.Integer('Codigo de envio', size = 20)
    alto = fields.Float('Alto (cm)', (3,2))
    ancho = fields.Float('Ancho (cm)', (3,2))
    largo = fields.Float('Largo (cm)', (3,2))
    peso = fields.Float('Peso (Kg)', (5,3))
    precio_envio = fields.Float('Precio €', compute="_value_envio", store=True)
    centro_id = fields.Many2one('mensajeria.centro', string='Centro de reparto', required=True)
    cliente_id = fields.Many2one('mensajeria.cliente', string='Cliente', required=True)
    repartidor_id = fields.Many2one('mensajeria.repartidor', string='Repartidor asignado', required=True)

    @api.depends('alto', 'ancho', 'largo', 'peso')
    def _value_envio(self):
        for record in self:
            record.precio_envio = float((((record.alto * record.ancho * record.largo) / 100) * record.peso) * 10)