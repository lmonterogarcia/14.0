# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api, _


class helpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'helpdesk_ticket_action'

    name = fields.Char('Nombre')
    date = fields.Date('Fecha')
    time = fields.Float(string='Tiempo')
    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='Ticket',
        )
    