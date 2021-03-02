# -*- coding: utf-8 -*-
# from odoo import http


# class Party(http.Controller):
#     @http.route('/party/party/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/party/party/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('party.listing', {
#             'root': '/party/party',
#             'objects': http.request.env['party.party'].search([]),
#         })

#     @http.route('/party/party/objects/<model("party.party"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('party.object', {
#             'object': obj
#         })
