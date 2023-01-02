odoo.define('dws_source_clickable.open_link', function (require) {
"use strict";

var AbstractField = require('web.AbstractField');
var core = require('web.core');
var field_registry = require('web.field_registry');

var _t = core._t;

var OpenLink = AbstractField.extend({
    events: _.extend({}, AbstractField.prototype.events, {
        'click .open_link': '_onClick',
    }),
    /**
     * @override
     */
    init: function () {
        this._super.apply(this, arguments);
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @private
     * @override
     */
    _renderReadonly: function () {
        self = this
        this._super.apply(this, arguments);
        var data = JSON.parse(this.value);
        _.each(data, function(key) {
            self.$el.append('<span class="open_link badge-pill badge-pill badge-light" style="cursor: pointer;background-color:#7c7bad;color:white;" id="'+key[0]+'" model="'+key[1]+'" clickable="'+key[3]+'">' +key[2]+ '</span>')
        });
    },
    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @private
     * @override
     */
    _onClick: function (e) {
        var $span = $(e.target);
        console.log($span)
        var res_id = $span[0].attributes.id.value
        var res_model = $span[0].attributes.model.value
        var click = $span[0].attributes.clickable.value
        if (res_model && res_id && click > 0) {
            this.do_action({
                type: 'ir.actions.act_window',
                res_model: res_model,
                res_id: parseInt(res_id),
                views: [[false, 'form']],
                target: 'current'
            });
        }
    },
});
field_registry
    .add('open_link', OpenLink)
});

