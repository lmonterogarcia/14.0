# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api, _


class helpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = 'helpdesk_ticket_tag'

    name = fields.Char('Nombre')
    ticket_ids = fields.Many2many(
        string='Tags',
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_tag_rel',
        column1='tag_id',
        column2='ticket_id',
    )
    
    @api.model
    def cron_delete_tag(self):
        tickets = self.search([('ticket_ids', '=', False)])
        tickets.unlink()