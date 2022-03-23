# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class campos_extras(models.Model):
    _inherit = 'sale.order'

    # orden_com = fields.Char(
    #     string="Orden de Compra",
    # )
    num_contrato = fields.Char(string="Número de Contrato",)
    cuenta_analitica_obra = fields.Many2one(
        comodel_name="account.analytic.account", string="Cuenta analítica Obra")
