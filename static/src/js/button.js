
odoo.define('css_js.button', function (require) {
    const registry  = require('web.widget_registry');
    const Dialog = require('web.Dialog');
    const Widget  = require('web.Widget');

    console.log('CALSS BOTON');
     $(document).on('click',"#button_share",function() {
        console.log("jd");
               Dialog.alert(
                this,
                'Has copiado la URL',
                {
                    title: 'Exito'
                }
             );

        });



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