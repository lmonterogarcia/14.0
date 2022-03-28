# -*- coding: utf-8 -*-
# from odoo import http


# class Mensajeria(http.Controller):
#     @http.route('/mensajeria/mensajeria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mensajeria/mensajeria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mensajeria.listing', {
#             'root': '/mensajeria/mensajeria',
#             'objects': http.request.env['mensajeria.mensajeria'].search([]),
#         })

#     @http.route('/mensajeria/mensajeria/objects/<model("mensajeria.mensajeria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mensajeria.object', {
#             'object': obj
#         })
