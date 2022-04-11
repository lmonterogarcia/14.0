# -*- coding: utf-8 -*-
{
    'name': "Lualca - Restringir código cuenta contable (GST)",

    'summary': """Extención del módulo account, restrigir el ingreso de código de cuenta contable""",

    'description': """Extención del módulo account para restringir como se crear el código de las cuentas contables""",

    'author': "Guadaltech",
    'website': "http://www.guadaltech.es",

    # Categories can be used to filter modules in modules listing
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'views/res_config_account_views.xml',
    ],
}
