# -*- coding: utf-8 -*-
__author__ = 'gzp'

import math

from odoo import models, fields, api


class Bangumi(models.Model):
    _name = 'bangumi.bangumi'
    _description = 'Bangumi'

    @api.multi
    def action_like(self):
        return self.write({'like': True})

    @api.multi
    def action_unlike(self):
        return self.write({'like': False})

    @api.multi
    @api.depends('release_date', 'update_cycle', 'total')
    def _compute_current(self):
        for record in self:
            today = fields.Date.today()
            dt = today - record.release_date
            if dt.days < 0:
                self.current = 0
                continue

            if record.update_cycle == 'weekly':
                current = round(dt.days / 7)
                record.current = current if current < record.total else record.total

            if record.update_cycle == 'monthly':
                month_dt = (today.year - record.release_date.year) * 12 + (today.month - record.release_date.month)
                record.current = month_dt if month_dt < record.total else record.total

            if record.update_cycle == 'quarterly':
                quarter_dt = (today.year - record.release_date.year) * 4 + (
                        math.ceil(today.month / 3) - math.ceil(record.release_date.month / 3))
                record.current = quarter_dt if quarter_dt < record.total else record.total

    name = fields.Char(string='Name', required=True)
    cover_image = fields.Binary(string='Cover image', attachment=True)
    current = fields.Integer(string='Current', compute='_compute_current')
    total = fields.Integer(string='Total', required=True)
    already_seen = fields.Integer(string='Already seen', default=0)
    score = fields.Float(string='Score', required=True, default=0.0)
    like = fields.Boolean(string='Like', default=False)

    category_id = fields.Many2one(
        'bangumi.category', string='Category', required=False
    )

    tag_ids = fields.Many2many(
        'bangumi.tag', 'bangumi_bangumi_tag_rel',
        'bangumi_id', 'tag_id',
        string='Bangumi Tags'
    )

    update_cycle = fields.Selection([
        ('weekly', 'Update weekly'),
        ('monthly', 'Update monthly'),
        ('quarterly', 'Update quarterly')
    ], string='Update cycle', required=True, default='weekly')

    release_date = fields.Date(string='Release date', default=fields.Date.today(), required=True)
