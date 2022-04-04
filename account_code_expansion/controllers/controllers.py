# -*- coding: utf-8 -*-
# from odoo import http


# class AccountCodeExpansion(http.Controller):
#     @http.route('/account_code_expansion/account_code_expansion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_code_expansion/account_code_expansion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_code_expansion.listing', {
#             'root': '/account_code_expansion/account_code_expansion',
#             'objects': http.request.env['account_code_expansion.account_code_expansion'].search([]),
#         })

#     @http.route('/account_code_expansion/account_code_expansion/objects/<model("account_code_expansion.account_code_expansion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_code_expansion.object', {
#             'object': obj
#         })
