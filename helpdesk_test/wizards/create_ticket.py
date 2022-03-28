# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class CreateTicket(models.TransientModel):
    _name = 'create.ticket'
    _description  = 'create_ticket'

    name = fields.Char('Nombre')
    
    def create_ticket(self):
        self.ensure_one()
        active_id = self._context.get('active_id', False)
        if  active_id and self._context.get('active_model') == 'helpdesk.ticket.tag':
            ticket = self.env['helpdesk.ticket'].create({
                'name' : self.name,
                'tag_ids' : [(6, 0, [active_id])]
            })
            action = self.env.ref('helpdesk_test.helpdesk_ticket_action').read()[0]
            action['res_id'] = ticket.id
            action['views'] = [(self.env.ref('helpdesk_test.helpdesk_ticket_form').id, 'form')] # Lanza el formulario con la id que se acaba de crear
            return action
        return {'type' : 'ir.actions.ac_window_close'} # Acción especial para cerrar la ventana ( Si no se hace nada)
