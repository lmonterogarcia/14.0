# -*- coding: utf-8 -*-
# from odoo import http


# class Megamarket(http.Controller):
#     @http.route('/megamarket/megamarket/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/megamarket/megamarket/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('megamarket.listing', {
#             'root': '/megamarket/megamarket',
#             'objects': http.request.env['megamarket.megamarket'].search([]),
#         })

#     @http.route('/megamarket/megamarket/objects/<model("megamarket.megamarket"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('megamarket.object', {
#             'object': obj
#         })
