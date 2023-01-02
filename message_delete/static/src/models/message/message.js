odoo.define('message_delete/static/src/models/message/message.js', function (require) {
'use strict';

    const { _lt } = require('web.core');
    const { registerInstancePatchModel,} = require('mail/static/src/model/model_core.js');

    registerInstancePatchModel('mail.message', 'message_delete/static/src/models/message/message.js', {
        /**
         * Launch unlink rpc
         */
        async unlinkMessage() {
            if (! confirm(_lt("Do you really want delete this message?"))) {return false};
            await this.env.services.rpc({
                model: 'mail.message',
                method: 'unlink',
                args: [[this.id]],
                context: {"message_delete": true},
            });
            return true;
        },
    });

});
        