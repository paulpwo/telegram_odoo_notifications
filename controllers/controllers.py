# -*- coding: utf-8 -*-
# from odoo import http


# class MyTelegram(http.Controller):
#     @http.route('/my_telegram/my_telegram/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_telegram/my_telegram/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_telegram.listing', {
#             'root': '/my_telegram/my_telegram',
#             'objects': http.request.env['my_telegram.my_telegram'].search([]),
#         })

#     @http.route('/my_telegram/my_telegram/objects/<model("my_telegram.my_telegram"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_telegram.object', {
#             'object': obj
#         })
