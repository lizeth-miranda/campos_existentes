# -*- coding: utf-8 -*-
{
    'name': 'Campos Extras',
    'version': '13.2',
    'author': 'Demsa',
    'website': '',
    'depends': ['base', 'purchase_requisition', 'account'],
    'data': [
        # security
        # data
        # demo
        # reports
        # groups
        "groups/compra_validar_botones.xml",
        "groups/inventario_validar_botones.xml",
        "groups/facturas_validar_botones.xml",
        "groups/boton_autorizar.xml",
        "groups/calidad_orden_Compra.xml",
        "groups/grupo_RH.xml",
        # views
        #'views/purchase_order.xml',
        #'views/stock_picking.xml',
        "views/purchase_requisition.xml",
        'views/account_move.xml',
        #'views/hr_employee.xml',
        'views/sale_order.xml',
        'views/hr_expense.xml',


    ],
}
