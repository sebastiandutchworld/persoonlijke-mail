odoo.define('message_delete/static/src/components/message/message.js', function (require) {
'use strict';

    const components = {Message: require('mail/static/src/components/message/message.js')};
    const { patch } = require('web.utils');

    patch(components.Message, 'message_delete/static/src/components/message/message.js', {
        /**
         * @private
         * @param {MouseEvent} ev
         */
        async _onMessageUnlink(ev) {
            ev.stopPropagation();
            const successUnlink = await this.message.unlinkMessage();
            if (successUnlink) {
                this.unmount();
            };
        },
    });

});
