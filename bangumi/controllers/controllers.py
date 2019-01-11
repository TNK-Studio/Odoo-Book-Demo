# -*- coding: utf-8 -*-
from odoo import http

# class Bangumi(http.Controller):
#     @http.route('/bangumi/bangumi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bangumi/bangumi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bangumi.listing', {
#             'root': '/bangumi/bangumi',
#             'objects': http.request.env['bangumi.bangumi'].search([]),
#         })

#     @http.route('/bangumi/bangumi/objects/<model("bangumi.bangumi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bangumi.object', {
#             'object': obj
#         })