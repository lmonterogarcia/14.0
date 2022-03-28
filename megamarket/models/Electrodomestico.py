from odoo import models, fields, api

class Classes(models.Model): 
    _name = 'megamarket.electrodomestico' 
    _description = 'MegaMarket Electrodomestico'

    name = fields.Char('Nombre', required=True, help="nombre del electrodomestico") 
    code = fields.Integer('Código', required=True)
    nation_id = fields.Many2one('res.country', 'Pais', required=True)
    purchase_value = fields.Float('Importe de compra',required=True)
    coin_id = fields.Many2one('res.currency', 'Moneda', required=True)
    sale_price = fields.Float('Precio de venta',required=True)
    