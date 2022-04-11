from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    change_code = fields.Boolean(string="Restrict ledger account codes", default=True)
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

    # Class method
    def _increase_code(self, code, code_len):
        FILL_WITH = "0"
        replacement = ""
        position = 4

        for n in range(self.max_field_len - code_len):
            replacement += FILL_WITH
        return code[0:position] + replacement + code[position:]

    def _decrease_code(self, code, company_id, code_len):
        code_result = code
        position = 4
        
        for n in range(code_len - self.max_field_len):
            if code_result[position] == "0":
                code_result = code_result[:position] + code_result[position + 1 :]
            else:
                raise ValidationError(
                    _(
                        "The company '{}' have the account chart '{}' that con not be decrease".format(
                            company_id.name, code
                        )
                    )
                )
        return code_result

    def _account_code_verification(self):
        if self.max_field_len != self.env["ir.config_parameter"].sudo().get_param(
            "account_account_max_field_len"
        ):
            accounts = self.env["account.account"].search([])
            for record in accounts:
                code_len = len(record.code.strip())
                if code_len != self.max_field_len:
                    if code_len < self.max_field_len:
                        record.write(
                            {
                                "code": self._increase_code(
                                    record.code.strip(), code_len
                                ),
                                "super_changed": True,
                                "change_code": self.change_code,
                                "max_field_len": self.max_field_len,
                                "special_character": self.special_character,
                            }
                        )
                    else:
                        record.write(
                            {
                                "code": self._decrease_code(
                                    record.code.strip(), record.company_id, code_len
                                ),
                                "super_changed": True,
                                "change_code": self.change_code,
                                "max_field_len": self.max_field_len,
                                "special_character": self.special_character,
                            }
                        )
                    record.code

    # Method to obtain the values of ResConfigSettings
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            change_code=self.env["ir.config_parameter"]
            .sudo()
            .get_param("account_account_change_code")
            or False,
            max_field_len=int(
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("account_account_max_field_len")
            )
            or 6,
            special_character=self.env["ir.config_parameter"]
            .sudo()
            .get_param("account_account_special_character")
            or ".",
        )
        return res

    # Methods to set the values in ResConfigSettings
    def set_values(self):
        self._account_code_verification()
        res = super(ResConfigSettings, self).set_values()
        self.env["ir.config_parameter"].set_param(
            "account_account_change_code", self.change_code
        )
        self.env["ir.config_parameter"].set_param(
            "account_account_max_field_len", self.max_field_len
        )
        self.env["ir.config_parameter"].set_param(
            "account_account_special_character", self.special_character
        )
        return res
