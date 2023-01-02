odoo.define('message_delete/static/src/models/messaging_initializer/messaging_initializer.js', function (require) {
'use strict';

    const { registerInstancePatchModel,} = require('mail/static/src/model/model_core.js');

    registerInstancePatchModel('mail.messaging_initializer', 'message_delete/static/src/models/messaging_initializer/messaging_initializer.js', {
        /*
        * Re-write to pass if the active user has rights to delete messages
        */
        async start() {
            await this._super();
            this.messaging.deleteRight = await this.env.services.rpc({
                model: 'res.users',
                method: 'has_group',
                args: ["message_delete.group_message_delete"],
            });
        },
    });    

});
