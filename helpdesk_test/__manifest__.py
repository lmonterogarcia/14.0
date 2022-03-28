# -*- coding: utf-8 -*-
{
    'name': "helpdesk_test",

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
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'data/delete_tag_cron.xml',
        'report/helpdesk_ticket_report_templates.xml',
        'report/res_partner_templates.xml',
        'views/helpdesk_ticket_view.xml',
        'wizards/create_ticket_views.xml',
        'views/helpdesk_ticket_tag_view.xml',
        'views/helpdesk_menu.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
