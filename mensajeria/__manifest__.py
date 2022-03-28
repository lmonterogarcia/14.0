# -*- coding: utf-8 -*-
{
    'name': "mensajeria",
    'summary': """Modulo para gestionar una mensajeria""",
    'description': """Modulo para una mensajeria para gestionar clientes, repartidores, centro de repoarto y envios""",
    'author': "Azahar Apps",
    'website': "http://www.luismontero.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_clientes.xml',
        'views/view_repartidores.xml',
        'views/view_centros.xml',
        'views/view_envios.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
