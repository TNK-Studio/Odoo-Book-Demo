# -*- coding: utf-8 -*-
__author__ = 'gzp'

import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class Category(models.Model):
    _name = 'bangumi.category'
    _description = 'Bangumi category'

    @api.model
    def _get_current_uid(self):
        _logger.info("Category model call _get_current_uid(%s)" % self)
        return self.env.uid

    name = fields.Char(string='Name', required=True)
    user_id = fields.Many2one(
        'res.users', string='User', required=True,
        default=_get_current_uid
    )
