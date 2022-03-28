# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Material(models.Model): 
    _name = 'gym.material' 
    _description = 'Material Classes'

    name = fields.Char(string="Nombre", required=True, help="nombre del material")
    purchase_date = fields.Date('Fecha de adquisición',required=True, autodate = True)
    weight = fields.Float('Peso KG', (5,3))
    activityType = fields.Selection([('movil','Móvil'),
                                    ('fijo','Fijo'),],
                                    'Tipo de material')
    classes_ids = fields.Many2many("gym.classes",string="Utilizado en clases")
        
 