# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class campos_extras(models.Model):
    _inherit = 'account.move'

    desc = fields.Char(
        string="descripción",
    )
