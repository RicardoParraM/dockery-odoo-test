# -*- coding: utf-8 -*-

from odoo import api, fields, models

# class dummy_module(models.Model):
#     _name = 'dummy_module.dummy_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
