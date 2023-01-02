from odoo import _, api, exceptions, fields, models, tools

class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'
   
    def _message_subscribe(self, partner_ids=None, channel_ids=None, subtype_ids=None, customer_ids=None):
        params = self.env['ir.config_parameter'].sudo()
        disable_followers = params.get_param('odoo_pragtech_disable_followers.disable_followers')
        if bool(disable_followers)==True:
            return False
        else:
            return super(MailThread, self)._message_subscribe(partner_ids, channel_ids, subtype_ids, customer_ids)

    
 
