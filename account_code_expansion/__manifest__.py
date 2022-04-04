# -*- coding: utf-8 -*-
{
    'name': "account_code_expansion",

    'summary': """Extencion del modulo account""",

    'description': """Extencion del modulo account para restringir como se crear el código de las cuentas contables""",

    'author': "Guadaltech",
    'website': "http://www.guadaltech.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_config_account_views.xml',
    ],
}
