# -*- coding: utf-8 -*-
{
    'name': "zoo",
    'summary': """Gestion de Zoo""",
    'description': """Gesuion de animales, cuidadores y espacios del ZOO """,
    'author': "Luis Montero",
    'website': "http://www.luismontero.es",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_animal.xml',
        'views/view_cuidador.xml',
        'views/view_espacio.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
