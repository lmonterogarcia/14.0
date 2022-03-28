# -*- coding: utf-8 -*-
{
    'name': "Project helpdesk_test",

    'summary': """Aplicacion de practica - helpdesk""",

    'description': """Aplicaciones para aprender a crear modulos""",

    'author': "Luis Montero - Guadaltech",
    'website': "http://www.guadaltech.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        'security/project_helpdesk_security.xml',
        'security/ir.model.access.csv',
        'data/project_helpdesk_data.xml',
        'views/project_helpdesk_ticket_view.xml',
        'views/project_helpdesk_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
