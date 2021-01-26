# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class campos_extras(models.Model):
    _inherit = 'stock.picking'

    numero_fatu = fields.Char(
        string="Número de Factura",
    )
    Origen_acuerdo = fields.Char(
        string="Origen Acuerdo Compra"
    )
    cuenta_ana = fields.Char(
        string="Cuenta Analitica",
    )
