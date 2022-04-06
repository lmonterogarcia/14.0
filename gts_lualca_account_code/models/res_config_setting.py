from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    change_code = fields.Boolean(
        string="Restringir códigos de las cuentas contables", default=True
    )
    max_field_len = fields.Integer(string="Longitud Máxima", default=6)
    special_character = fields.Char(string="Caracter Especial", default=".", size=1)


    # Constraints para que no se pueda crear una cuenta con un código que no cumpla con las condiciones
    @api.constrains("max_field_len")
    def _check_fill_with(self):
        for record in self:
            if record.max_field_len < 6 or record.max_field_len > 30:
                raise ValidationError(
                    _(
                        "El campo 'Longitud Máxima' tiene que ser un dígito y estar en el rango de 6 a 30"
                    )
                )

    # Metodo para obtener los valores de ResConfigSettings
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            change_code = self.env["ir.config_parameter"].sudo().get_param('account.account.change_code') or True,
            max_field_len = int(self.env["ir.config_parameter"].sudo().get_param('account.account.max_field_len')) or 6,
            special_character = self.env["ir.config_parameter"].sudo().get_param('account.account.special_character') or '.',
        )
        return res

    # Metodos para setear los valores en ResConfigSettings
    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env["ir.config_parameter"].set_param(
            "account.account.change_code", self.change_code
        )
        self.env["ir.config_parameter"].set_param(
            "account.account.max_field_len", self.max_field_len
        )
        self.env["ir.config_parameter"].set_param(
            "account.account.special_character", self.special_character
        )
        return res
