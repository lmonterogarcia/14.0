# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class ProjectHelpdeskTicket(models.Model):
    _name = 'project.helpdesk.ticket'
    _description = 'project_helpdesk_ticket'
    _inherits = {'project.task': 'task_id'}
    
    @api.model
    def default_get(self, fields):
        defaults = super(ProjectHelpdeskTicket, self).default_get(fields)
        defaults.update({
            'project_id' : self.env.ref('project_helpdesk_test.project_helpdesk').id
        })
        return defaults
    
    task_id = fields.Many2one(
        string='Tarea', 
        comodel_name='project.task',
        auto_join=True,
        index=True,
        ondelete='cascade',
        required=True)
    action_corrective = fields.Html(
        string='Acción correctora',
        help='Acciones correctoras por hacer'
        )
    action_preventive = fields.Html(
        string='Acción preventivas',
        help='Acciones preventivas por hacer'
        )
    
    def action_assign_to_me(self):
        self.ensure_one()
        return self.task_id.action_assign_to_me
    
    def action_subtask(self):
        self.ensure_one()
        return self.task_id.action_subtask()
    
    def action_recurring_tasks(self):
        self.ensure_one()
        return self.task_id.action_recurring_tasks()
    
    def _message_get_suggested_recipients(self):
        self.ensure_one()
        return self.task_id._message_get_suggested_recipients()