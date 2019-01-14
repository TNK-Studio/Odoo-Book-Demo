# -*- coding: utf-8 -*-
__author__ = 'gzp'

from odoo import models, fields, api


class Bangumi(models.Model):
    _name = 'bangumi.bangumi'
    _description = 'Bangumi'

    name = fields.Char(string='Name', required=True)
    total = fields.Integer(string='Total', required=True)
    already_seen = fields.Integer(string='Already seen', default=0)
    score = fields.Float(string='Score', required=True, default=0.0)

    category_id = fields.Many2one(
        'bangumi.category', string='Category', required=False
    )

