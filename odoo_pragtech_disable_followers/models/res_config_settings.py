from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'
    
    disable_followers=fields.Boolean("Disable Followers")
    
    @api.model
    def get_values(self):
        '''This method is getter method to get current boolean value for defined fields.'''
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        disable_followers = params.get_param('odoo_pragtech_disable_followers.disable_followers', default=False)
        res.update(disable_followers=disable_followers)
        return res
    
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param("odoo_pragtech_disable_followers.disable_followers", self.disable_followers)