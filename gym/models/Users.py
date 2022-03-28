# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Users(models.Model): 
    _name = 'gym.users' 
    _description = 'Users Classes'

    name = fields.Char(string="Nombre", size=60, required=True, help="Nombre del usuario")
    idcard = fields.Char('DNI', size=9, required=True)
    photo=fields.Binary('Foto')
    classes_ids = fields.Many2many("gym.classes",string="Clases")
    pago_id = fields.One2many('gym.pago', 'user_ids', string='Pagos')