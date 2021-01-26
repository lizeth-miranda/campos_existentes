# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class campos_extras(models.Model):
    _inherit = 'hr.employee'

    cod_emp = fields.Char(
        string="Código Empleado",
    )
    fecha_ingr = fields.Date(
        string="Fecha de Ingreso"
    )
    registro_imss = fields.Char(
        string="Registro del IMSS",
    )
