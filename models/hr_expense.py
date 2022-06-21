# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class acuerdo_compra(models.Model):
    _inherit = 'hr.expense'

    total_amount_negative = fields.Monetary(compute="amount_negative")

    def amount_negative(self):
        for record in self:
            record.total_amount_negative = (record.total_amount) * -1

    def send_cuenta_analitica(self):

        for record in self:

            self.env['account.analytic.line'].create({
                'date': record.date,
                'name': record.product_id.name,
                'account_id': record.analytic_account_id.id,
                'amount': record.total_amount_negative,
            })
