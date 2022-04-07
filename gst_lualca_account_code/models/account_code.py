from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountCode(models.Model):
    """Module to improve the way a code is create and write in account.account module.

    Depending on the desired length, the special character used you want
    to fill the account.account code, it will return a char, and store it
    in System Parameter.
    """

    _inherit = "account.account"

    def _change_code(self, vals):

        FILL_WITH = "0"

        change_code = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("account.account.change_code")
        )
        max_field_len = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("account.account.max_field_len")
        )
        special_character = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("account.account.special_character")
        )

        if change_code and "code" in vals:
            if len(vals["code"]) > int(
                max_field_len
            ):  # max_field_len comes in the form of a String so parse it to int
                raise ValidationError(
                    _(
                        'The code cannot have more than {} digits counting "{}"'.format(
                            max_field_len, special_character
                        )
                    )
                )
            elif vals["code"].isdigit():
                vals["code"] = (
                    len(vals["code"]) == int(max_field_len)
                    and vals["code"]
                    or vals["code"].ljust(int(max_field_len), FILL_WITH)
                )  # Leave it as it is or complete a string with a character at the end until reaching a certain length
            elif (
                special_character in vals["code"]
                and vals["code"].count(special_character) == 1
                and len(vals["code"]) > 1
            ):
                replacement = ""
                for n in range(
                    int(max_field_len) - (len(vals["code"]) - 1)
                ):  # max_field_len comes in the form of a String so parse it to int
                    replacement += FILL_WITH

                vals["code"] = vals["code"].replace(special_character, replacement)

            else:
                raise ValidationError(_("The code is not correct"))

        return vals

    @api.model
    def create(self, vals):
        return super().create(self._change_code(vals))

    def write(self, vals):
        return super().write(self._change_code(vals))
