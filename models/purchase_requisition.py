# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class acuerdo_compra(models.Model):
    _inherit = "purchase.requisition"

    #state = fields.Selection(selection_add=[(
        #"Autorizar", "Autorizado"), ("ongoing",)])
    #state_blanket_order = fields.Selection(selection_add=[(
        #"Autorizar", "Autorizado"), ("ongoing",)])
    
    usuario = fields.Many2one(
        'res.users', string='Usuario',
        default=lambda self: self.env.user)
    
    #def action_autorizar(self):
        #self.write({'state': 'Autorizar'})

    #doc_ori = fields.Many2one('Documento Origen Prueba', 'documento.origen',)
    #notas = fields.Text(string="Notas",)
