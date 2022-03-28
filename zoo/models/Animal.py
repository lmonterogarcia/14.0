# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Animal(models.Model):
    _name = 'zoo.animal'
    _description = 'Clase Animal'
    
    name = fields.Char('Nombre', required=True)
    species = fields.Char('Especie')
    animal_id = fields.Integer('Código', required=True)
    country_id = fields.Many2one('res.country','País de procedencia')
    age = fields.Integer('Edad')
    date_entry = fields.Date('Fecha entrada en el Zoo', required=True, autodate =True)