from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"
    special_codes = (
        "1034",
        "1044",
        "1141",
        "1142",
        "1143",
        "1144",
        "1371",
        "1533",
        "1534",
        "1535",
        "1536",
        "1543",
        "1544",
        "1545",
        "1546",
        "1603",
        "1604",
        "1605",
        "1613",
        "1614",
        "1615",
        "1623",
        "1624",
        "1625",
        "1633",
        "1634",
        "1635",
        "2403",
        "2404",
        "2405",
        "2413",
        "2414",
        "2415",
        "2423",
        "2424",
        "2425",
        "2493",
        "2494",
        "2495",
        "2801",
        "2802",
        "2803",
        "2805",
        "2806",
        "2811",
        "2812",
        "2813",
        "2814",
        "2815",
        "2816",
        "2817",
        "2818",
        "2819",
        "2901",
        "2902",
        "2903",
        "2905",
        "2906",
        "2911",
        "2912",
        "2913",
        "2914",
        "2915",
        "2916",
        "2917",
        "2918",
        "2919",
        "2921",
        "2933",
        "2934",
        "2935",
        "2943",
        "2944",
        "2945",
        "2953",
        "2954",
        "2955",
        "4004",
        "4009",
        "4031",
        "4034",
        "4036",
        "4039",
        "4104",
        "4109",
        "4301",
        "4304",
        "4309",
        "4311",
        "4312",
        "4315",
        "4331",
        "4332",
        "4334",
        "4336",
        "4337",
        "4339",
        "4404",
        "4409",
        "4411",
        "4412",
        "4415",
        "4708",
        "4709",
        "4742",
        "4745",
        "4751",
        "4752",
        "4758",
        "4759",
        "4933",
        "4934",
        "4935",
        "4994",
        "4999",
        "5095",
        "5103",
        "5104",
        "5105",
        "5113",
        "5114",
        "5115",
        "5123",
        "5124",
        "5125",
        "5133",
        "5134",
        "5135",
        "5143",
        "5144",
        "5145",
        "5201",
        "5208",
        "5209",
        "5291",
        "5292",
        "5293",
        "5295",
        "5296",
        "5297",
        "5303",
        "5304",
        "5305",
        "5313",
        "5314",
        "5315",
        "5323",
        "5324",
        "5325",
        "5333",
        "5334",
        "5335",
        "5343",
        "5344",
        "5345",
        "5353",
        "5354",
        "5355",
        "5393",
        "5394",
        "5395",
        "5523",
        "5534",
        "5525",
        "5563",
        "5564",
        "5565",
        "5566",
        "5585",
        "5593",
        "5595",
        "5598",
        "5933",
        "5934",
        "5935",
        "5943",
        "5944",
        "5945",
        "5953",
        "5954",
        "5955",
        "6061",
        "6062",
        "6081",
        "6082",
        "6091",
        "6092",
        "6301",
        "6341",
        "6342",
        "6391",
        "6392",
        "6457",
        "6511",
        "6611",
        "6612",
        "6613",
        "6615",
        "6616",
        "6617",
        "6618",
        "6621",
        "6622",
        "6623",
        "6624",
        "6641",
        "6642",
        "6643",
        "6651",
        "6652",
        "6653",
        "6654",
        "6655",
        "6656",
        "6657",
        "6661",
        "6662",
        "6663",
        "6665",
        "6666",
        "6667",
        "6668",
        "6671",
        "6672",
        "6673",
        "6675",
        "6676",
        "6677",
        "6678",
        "6733",
        "6734",
        "6735",
        "6931",
        "6932",
        "6933",
        "6954",
        "6959",
        "6961",
        "6962",
        "6963",
        "6965",
        "6966",
        "6967",
        "6968",
        "6971",
        "6972",
        "6973",
        "6981",
        "6985",
        "6986",
        "6987",
        "6988",
        "6991",
        "6992",
        "6993",
        "7001",
        "7002",
        "7011",
        "7012",
        "7021",
        "7022",
        "7031",
        "7032",
        "7041",
        "7042",
        "7051",
        "7052",
        "7061",
        "7062",
        "7063",
        "7081",
        "7082",
        "7083",
        "7084",
        "7091",
        "7092",
        "7093",
        "7094",
        "7461",
        "7511",
        "7601",
        "7602",
        "7603",
        "7611",
        "7612",
        "7613",
        "7620",
        "7621",
        "7631",
        "7632",
        "7633",
        "7661",
        "7662",
        "7663",
        "7665",
        "7666",
        "7667",
        "7668",
        "7733",
        "7734",
        "7735",
        "7931",
        "7932",
        "7933",
        "7951",
        "7952",
        "7954",
        "7955",
        "7956",
        "7957",
        "7961",
        "7962",
        "7963",
        "7965",
        "7966",
        "7967",
        "7968",
        "7971",
        "7972",
        "7973",
        "7981",
        "7985",
        "7986",
        "7987",
        "7988",
        "7991",
        "7992",
        "7993",
    )

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

        # if not code[:4] in self.special_codes:
        #     position = 3

        for n in range(self.max_field_len - code_len):
            replacement += FILL_WITH
        return code[0:position] + replacement + code[position:]

    def _decrease_code(self, code, company_id, code_len):
        code_result = code
        position = 4

        # if not code[:4] in self.special_codes:
        #     position = 3

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
