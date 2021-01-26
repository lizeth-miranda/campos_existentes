# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class campos_extras(models.Model):
    _inherit = 'purchase.order'

    numero_fact = fields.Char(
        string="Numero de Factura",
    )
