# -*- coding: utf-8 -*-
from odoo import http

# class DummyModule(http.Controller):
#     @http.route('/dummy_module/dummy_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dummy_module/dummy_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dummy_module.listing', {
#             'root': '/dummy_module/dummy_module',
#             'objects': http.request.env['dummy_module.dummy_module'].search([]),
#         })

#     @http.route('/dummy_module/dummy_module/objects/<model("dummy_module.dummy_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dummy_module.object', {
#             'object': obj
#         })