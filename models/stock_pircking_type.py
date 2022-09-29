# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class campos_extras(models.Model):
    _inherit = 'stock.picking.type'

    user_almacen = fields.Many2many(
        'res.users', string='Responsables Almacen')
