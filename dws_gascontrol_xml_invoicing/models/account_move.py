# Copyright 2016-2017 Akretion (http://www.akretion.com)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# Copyright 2019 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import base64
import logging

from lxml import etree

from odoo import models
from odoo.tools import float_is_zero, float_round

logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _name = "account.move"
    _inherit = ["account.move", "base.ubl"]

    def return_ubl_xml_file(self):
        self.ensure_one()
        assert self.move_type in ("out_invoice", "out_refund")
        assert self.state == "posted"
        version = self.get_ubl_version()
        xml_string = base64.b64encode(self.generate_ubl_xml_string(version=version))
        
        return xml_string



