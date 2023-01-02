# -*- coding: utf-8 -*-

from odoo import api, models
# from odoo.tools import pycompat
from odoo.tools import pdf
from odoo.exceptions import AccessError
import base64
import re

class MailTemplate(models.Model):
    _inherit = 'mail.template'

    def generate_email(self, res_ids, fields):
        rslt = super(MailTemplate, self).generate_email(res_ids, fields) #inherits existing 

        multi_mode = True       #allows multiple models to be called to avoid singleton error
        if isinstance(res_ids, int):
            res_ids = [res_ids]
            multi_mode = False

        for res_id in res_ids:  #loops through all model ID's
            related_model = self.env[self.model_id.model].browse(res_id) #creates an object of the model 

            if related_model._name == 'account.move': #if model object is account.move execute function
                attachments_list = multi_mode and rslt[res_id]['attachments'] or rslt['attachments'] # returns list value of attachmenst
                if related_model.partner_id.lang == 'nl_NL':                
                    rslt[res_id]['attachments'].append(("Factuur_" + related_model.name.replace("/", "_") + ".xml", related_model.return_ubl_xml_file()))
                if related_model.partner_id.lang == 'en_US':
                    rslt[res_id]['attachments'].append(("Invoice_" + related_model.name.replace("/", "_") + ".xml", related_model.return_ubl_xml_file()))
                if related_model.partner_id.lang == 'de_DE':
                    rslt[res_id]['attachments'].append(("Rechnung_" + related_model.name.replace("/", "_") + ".xml", related_model.return_ubl_xml_file()))

    

        return rslt

    
