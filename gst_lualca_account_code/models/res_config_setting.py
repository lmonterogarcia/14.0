from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    change_code = fields.Boolean(
        string="Restrict ledger account codes", default=True
    )
    max_field_len = fields.Integer(string="Maximum length", default=6)
    special_character = fields.Char(string="Special Character", default=".", size=1)


    # Constraints so that an account cannot be created with a code that does not meet the conditions
    @api.constrains("max_field_len")
    def _check_fill_with(self):
        for record in self:
            if record.max_field_len < 6 or record.max_field_len > 30:
                raise ValidationError(
                    _(
                        "The 'Maximum Length' field must be a digit and be in the range 6 to 30"
                    )
                )

    # Method to obtain the values of ResConfigSettings
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            change_code = self.env["ir.config_parameter"].sudo().get_param('account.account.change_code') or False,
            max_field_len = int(self.env["ir.config_parameter"].sudo().get_param('account.account.max_field_len')) or 6,
            special_character = self.env["ir.config_parameter"].sudo().get_param('account.account.special_character') or '.',
        )
        return res

    # Methods to set the values in ResConfigSettings
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
