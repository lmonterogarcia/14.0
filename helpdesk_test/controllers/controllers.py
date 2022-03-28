# -*- coding: utf-8 -*-
# from odoo import http


# class HelpdeskTest(http.Controller):
#     @http.route('/helpdesk_test/helpdesk_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/helpdesk_test/helpdesk_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('helpdesk_test.listing', {
#             'root': '/helpdesk_test/helpdesk_test',
#             'objects': http.request.env['helpdesk_test.helpdesk_test'].search([]),
#         })

#     @http.route('/helpdesk_test/helpdesk_test/objects/<model("helpdesk_test.helpdesk_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helpdesk_test.object', {
#             'object': obj
#         })
