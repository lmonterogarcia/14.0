# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Espacio(models.Model):
    _name = 'zoo.espacio'
    _description = 'Clase Espacio de zoo'
    
    code = fields.Integer('Código', required=True)
    type_space = fields.Selection([('jaula','Jaula'),
                                    ('vallado','Vallado'),
                                    ('acuario','Acuario'),
                                    ('terrarium','Terrarium')],
                                    'Tipo de zona', required=True)
    tematic_area = fields.Selection([('europa','Europa'),
                                    ('asia','Asia'),
                                    ('africa','África'),
                                    ('america','Ámerica'),
                                    ('oceania','Oceanía')],
                                    'Área temática', required=True)