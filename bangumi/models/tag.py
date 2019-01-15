# -*- coding: utf-8 -*-
__author__ = 'gzp'

from odoo import models, fields


class Tag(models.Model):
    _name = 'bangumi.tag'
    _description = 'Bangumi tag'

    name = fields.Char(string='Name', required=True)
    user_id = fields.Many2one(
        'res.users', string='User', required=True,
        default=lambda self: self.env.uid
    )

    bangumi_ids = fields.Many2many(
        'bangumi.bangumi', 'bangumi_bangumi_tag_rel',
        'tag_id', 'bangumi_id',
        string='Tag Bangumi Set'
    )
