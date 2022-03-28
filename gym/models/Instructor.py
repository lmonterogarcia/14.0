# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Instructores(models.Model): 
    _name = 'gym.instructores' 
    _description = 'Instructors Classes'

    name = fields.Char(string="Nombre", size=60, required=True, help="Nombre del instructor")
    idcard = fields.Char('DNI', size=9, required=True) 
    photo=fields.Binary('Foto')
    gymclass_ids = fields.One2many('gym.classes','instructores_id', 'Clases')
