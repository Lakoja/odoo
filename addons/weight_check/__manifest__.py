# -*- coding: utf-8 -*-
{
    'name': "Manual weight check (for DHL)",

    'summary': """
        Presents a dialog if a manual weight check has not been performed, yet.""",

    'author': "Ulrich Kuhn",
    'website': "https://github.com/Lakoja/odoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'module_category_inventory',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'delivery'],

    'data': [
        'security/ir.model.access.csv',
        'wizard/enter_manual_weight.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
