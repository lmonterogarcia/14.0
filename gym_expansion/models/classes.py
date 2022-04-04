from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ClassesExtension(models.Model):
    """Module to improve the way a code is create and write in account.account module.

    Depending on the desired length, the special character used and the character
    as you want to fill the account.account code, it will return a char, and store it
    in account.account.code.
    """

    _inherit = "gym.classes"

    code = fields.Char(string="Código", required=True)

    def _change_code(self, vals):

        """Variables que irán en Contabilidad->Ajustes"""
        change_code = True
        fill_with = "0"
        max_field_len = 8
        especial_character = "."

        if change_code:
            if len(vals["code"]) > 8:
                raise ValidationError(
                    _(
                        'El código no puede tener más de {} dígitos contando con "{}"'.format(
                            max_field_len, especial_character
                        )
                    )
                )
            elif vals["code"].isdigit():
                vals["code"] = (
                    len(vals["code"]) == 8
                    and vals["code"]
                    or vals["code"].ljust(max_field_len, fill_with)
                )  # Lo deja tal cual o completa un string con un caracter al final hasta llegar a un length determinado
            elif (
                especial_character in vals["code"]
                and vals["code"].count(especial_character) == 1
                and len(vals["code"]) > 1
            ):
                replacement = ""
                for n in range(max_field_len - (len(vals["code"]) - 1)):
                    replacement += fill_with
                vals["code"] = vals["code"].replace(especial_character, replacement)
            else:
                raise ValidationError(_("El código no es correcto"))

        return vals

    @api.model
    def create(self, vals):
        return super().create(self._change_code(vals))

    def write(self, vals):
        return super().write(self._change_code(vals))