# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta


class helpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'helpdesk_ticket'
    _inherit=[
        'mail.thread.cc',
        'mail.thread.blacklist',
        'mail.activity.mixin']
    _primary_email = 'email_from'
    
    # metodos para campos default
    def _date_default_today(self):
        return fields.Date.today()
    
    def _user_id_default_current(self):
        return self.env.uid
    
    name = fields.Char(
        string='Nombre',
        required=True
        )
    description = fields.Text('Descripción')
    date = fields.Date(string='Fecha', default=_date_default_today)
    state = fields.Selection(
        [('new', 'Nuevo'),
         ('assigned', 'Asignado'),
         ('in_process', 'En Proceso'),
         ('pending', 'Pendiente'),
         ('resolved', 'Resuelto'),
         ('canceled', 'Cancelado'),],
        string='Estados', 
        default='new')
    time = fields.Float(
        string = 'Tiempo', 
        compute ='_get_time', 
        inverse='_set_time',
        search='_search_time')
    assigned = fields.Boolean(
        string='Asigando',
        compute='_compute_assigned',)
    date_limit = fields.Date(string='Fecha límite')
    action_corrective = fields.Html(
        string='Acción correctora',
        help='Acciones correctoras por hacer')
    action_preventive = fields.Html(
        string='Acción preventivas',
        help='Acciones preventivas por hacer')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Asignado a',
        default=_user_id_default_current)
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id', 
        string='Acción')
    tag_ids = fields.Many2many(
        string='Tag',
        comodel_name='helpdesk.ticket.tag',
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id')
    partner_id = fields.Many2one(string='Socio', comodel_name='res.partner')
    email_from = fields.Char(string='email_from')
    
    def do_assig(self):
        self.ensure_one()
        self.write({
         'state':'assigned',
         'assigned':True})
        # for ticket in self:
        #     ticket.state = 'assigned'
        #     ticket.assigned = True
        
    def process(self):
        self.ensure_one()
        self.state = 'in_process'
        
    def pending(self):
        self.ensure_one()
        self.state = 'pending'
        
    def resolved(self):
        self.ensure_one()
        self.state = 'resolved'
        
    def cancel(self):
        self.ensure_one()
        self.state = 'canceled'
        
    def cancel_multi(self):
        for record in self:
            record.cancel()
        
    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = self.user_id and True or False #Si tiene asignado un user_id es true si no false
            
    # la cantuidad de tickets asociados al mismo usuario
    ticket_qty = fields.Integer(
        string = 'Cantidad de Ticket',
        compute = '_compute_ticket_qty')
    
    @api.depends('user_id')
    def _compute_ticket_qty(self):
        for record in self:
            other_tickets = self.env['helpdesk.ticket'].search([('user_id', '=', record.user_id.id)])
            record.ticket_qty = len(other_tickets)
            
    #crear un campo nombre de etiqueta, y hacer un botón qyue cree la nueva etiqueta con ese nombre yb lo asocie al ticket
    tag_name = fields.Char(
        string = 'Tag Name'
    )
    
    def create_tag(self):
        self.ensure_one()
        #import pdb; pdb.set_trace()
        #import wdb; wdb.set_trace()
        #opción 1
        # self.write({
        #     'tag_ids' : [(0,0, {'name' : self.tag_name})]
        # })
        
        # #opción 2
        # tag = self.env['helpdesk.ticket.tag'].create({
        #     'name' : self.tag_name
        # })
        # self.wirte({
        #     'tag_ides' : [(4,tag.id,0)]
        # })
        
        # #opción 3
        # tag = self.env['helpdesk.ticket.tag'].create({
        #     'name' : self.tag_name
        # })
        # self.wirte({
        #     'tag_ides' : [(6,0,tag.ids)]
        # })
        
        # #opción 4
        # tag = self.env['helpdesk.ticket.tag'].create({
        #     'name' : self.tag_name,
        #     'ticket_ids' : [(6,0,self.ids)]
        #})
        #self.tag_name = False
        
        # Modificar el botón de crear una etiqueta en el formulario de ticket para que abra una acción nueva, pasando por contexto el valor del nombre y la relación con el ticket.
        action = self.env.ref('helpdesk_test.action_new_tag').read()[0]
        action['context'] = {
            'default_name': self.tag_name,
            'default_ticket_ids': [(6, 0, self.ids)]
        }
        # action['res_id'] = tag.id
        self.tag_name = False
        return action

    @api.constrains("time")
    def _check_time(self):
        for record in self:
            if record.time and (record.time <= 0 or record.time >= 8):
                raise ValidationError(_("El tiempo tiene que ser un número mayor que cero y menor que ocho"))
        
    
    @api.onchange("date")
    def _onchange_date(self):
        if self.date:
            self.date_limit = self.date + timedelta(days=1)
    
    #Campos invertidos calculados
    @api.depends('action_ids.time')
    def _get_time(self):
        for record in self:
            record.time = sum(record.action_ids.mapped('time'))
    
    def _set_time(self):
        for record in self:
            if record.time:
                time_now = sum(record.action_ids.mapped('time'))
                next_time = record.time - time_now
                if next_time:
                    data = {'name' : '/', 'time' : next_time, 'date' : fields.Date.today(), 'ticket_id' : record.id}
                    self.env['helpdesk.ticket.action'].create(data)

    def _search_time(self, operator, value):
        actions = self.env['helpdesk.ticket.action'].search([('time', operator, value)])
        return [('id', 'in', actions.mapped('ticket_id').ids)]
                    
# (0, 0,  { values })    link to a new record that needs to be created with the given values dictionary
# (1, ID, { values })    update the linked record with id = ID (write *values* on it)
# (2, ID)                remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)
# (3, ID)                cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)
# (4, ID)                link to existing record with id = ID (adds a relationship)
# (5)                    unlink all (like using (3,ID) for all linked records)
# (6, 0, [IDs])          replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)