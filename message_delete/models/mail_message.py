# -*- coding: utf-8 -*-

from odoo import _, models
from odoo.exceptions import AccessError


class mail_message(models.Model):
    """
    Overwrite to make sure unlink is done by ERP managers
    """
    _name = 'mail.message'
    _inherit = 'mail.message'

    def unlink(self):
        """
        Overwrite to add the extra security check
        """
        if self._context.get('message_delete'):
            if not self.env.user.has_group("message_delete.group_message_delete"):
                raise AccessError((_("""To delete messages the right 'Message Deleting' is required. 
                      Please contact your system administrator""")))
        return super(mail_message, self).unlink()
