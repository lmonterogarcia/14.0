# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cuidador(models.Model):
    _name = 'zoo.cuidador'
    _description = 'Clase Cuidador'
    
    name = fields.Char('Nombre', required=True)
    surname = fields.Char('Apellidos')
    work_position = fields.Selection([('supervisor','Supervisor'),
                                    ('manager','Encargado'),
                                    ('carer','Cuidador')],
                                    'Cargo')
    date_entry = fields.Date('Fecha incorporación a la empresa', required=True, autodate =True)