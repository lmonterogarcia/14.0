from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    change_code = fields.Boolean(
        string="Restringir códigos de las cuentas contables", default=True
    )
    fill_with = fields.Char(string="Dígito de Relleno", default="0", size=1)
    max_field_len = fields.Integer(string="Longitud Máxima", default=6)
    special_character = fields.Char(string="Caracter Especial", default=".", size=1)
    special_account = fields.Char(string="Cuenta Especial", default="430", size=3)

    # Constraints para que no se pueda crear una cuenta con un código que no cumpla con las condiciones
    @api.constrains("fill_with")
    def _check_fill_with(self):
        for record in self:
            if not record.fill_with.isdigit():
                raise ValidationError(
                    _("El campo 'Dígito de relleno' tiene que ser un solo número")
                )

    @api.constrains("max_field_len")
    def _check_fill_with(self):
        for record in self:
            if record.max_field_len < 6 or record.max_field_len > 30:
                raise ValidationError(
                    _(
                        "El campo 'Longitud Máxima' tiene que ser un dígito y estar en el rango de 6 a 30"
                    )
                )

    @api.constrains("special_account")
    def _check_fill_with(self):
        for record in self:
            if len(record.special_account) != 3:
                raise ValidationError(
                    _("El campo 'Cuenta Especial' tiene que ser un número de 3 dígito")
                )

    # # Metodo para obtener los valores de ResConfigSettings
    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()
    #     res.update(
    #         change_code = self.env.ref('account.account.change_code'),
    #         fill_with = self.env.ref('account.account.fill_with'),
    #         max_field_len = self.env.ref('account.account.max_field_len'),
    #         special_character = self.env.ref('account.account.special_character'),
    #         special_account = self.env.ref('account.account.special_account'),
    #     )
    #     return res

    # Metodos para setear los valores en ResConfigSettings
    def set_values_change_code(self):
        super(ResConfigSettings, self).set_values()
        if self.change_code:
            self.env["ir.config_parameter"].set_param(
                "account.account.change_code", self.change_code
            )

    def set_values_fill_with(self):
        super(ResConfigSettings, self).set_values()
        if self.fill_with:
            self.env["ir.config_parameter"].set_param(
                "account.account.fill_with", self.fill_with
            )

    def set_values_max_field_len(self):
        super(ResConfigSettings, self).set_values()
        if self.max_field_len:
            self.env["ir.config_parameter"].set_param(
                "account.account.max_field_len", self.max_field_len
            )

    def set_values_special_character(self):
        super(ResConfigSettings, self).set_values()
        if self.special_character:
            self.env["ir.config_parameter"].set_param(
                "account.account.special_character", self.special_character
            )

    def set_values_special_account(self):
        super(ResConfigSettings, self).set_values()
        if self.special_account:
            self.env["ir.config_parameter"].set_param(
                "account.account.special_account", self.special_account
            )
