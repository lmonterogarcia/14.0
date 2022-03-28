# -*- coding: utf-8 -*-
{
    'name': "megamarket",
    'summary': """Gestion del modulo MegaMarket""",
    'description': """Gestion de los electrodomesticos y los clientes""",
    'author': "TSI - UPO",
    'website': "http://www.upo.es",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_electrodomestico.xml',
        'views/view_cliente.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
