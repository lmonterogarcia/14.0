# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Classes(models.Model): 
    _name = 'gym.classes' 
    _description = 'Gym Classes'

    name = fields.Char(string="Titulo", required=True, help="nombre del gimnasio") 
    description = fields.Text('Descripción')
    start = fields.Datetime('Comieza',required=True)
    end = fields.Datetime('Termina',required=True)
    capacity = fields.Integer("Capacidad")
    activityType = fields.Selection([('dance','Baile'),
                                    ('aerobic','Aerobico'),
                                    ('anaerobic','Anaerobico'),
                                    ('relax','Relajante'),],
                                    'Tipo de actividad')
    users_ids = fields.Many2many("gym.users",string="Usuarios confirmados")
    instructores_id = fields.Many2one('gym.instructores',string="Instructor")
    material_ids = fields.Many2many("gym.material",string="Material usado")
        
 