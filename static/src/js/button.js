
odoo.define('css_js.button', function (require) {
    const registry  = require('web.widget_registry');
    const Dialog = require('web.Dialog');
    const Widget  = require('web.Widget');

    const WidgetButton = Widget.extend({
        selector: '.js_class',
        events: {
            'click button': 'clickEvent',
        },
        clickEvent (ev) {
            Dialog.alert(
                this,
                'Has copiado la URL',
                {
                    title: 'Exito'
                }
             );

        },

    });

    registry.WidgetButton = WidgetButton;
    console.log('is ready listo');

});