# -*- coding: utf-8 -*-
{
    'name': "sale_helpdesk_test",

    'summary': """Aplicacion de practica - sale helpdesk""",

    'description': """Aplicaciones para aprender a crear modulos heredados""",

    'author': "Luis Montero - Guadaltech",
    'website': "http://www.guadaltech.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'helpdesk_test'],

    # always loaded
    'data': [
        "report/sale_report_template.xml",
        "views/helpdesk_ticket_view.xml",
        "views/product_product_view.xml",
        "views/sale_order_view.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
