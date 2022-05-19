
odoo.define('css_js.button', function (require) {
    function resolveAfter2Seconds() {
      return 5;
    }

    async function asyncCall() {
      console.log('calling');
      const result = await resolveAfter2Seconds();
      console.log(result);
      console.log('calling');
      // expected output: "resolved"
    }

    asyncCall();

    const registry  = require('web.widget_registry');
    const Dialog = require('web.Dialog');
    const Widget  = require('web.basic_fields').FieldChar;



    const WidgetButton = Widget.extend({
        selector: '.js_class',
        events: {
            'click button': 'clickEvent',
        },
//        start () {
//            this._super.apply(this, arguments);
//            this.button = this.el.querySelector('button');
//            new ClipboardJS(this.el, {
//                text: () => document.location.origin + this.button.dataset.url,
//            });
//        },
//        async clickEvent (ev) {
//            await this._rpc({
//                route: '/academy/share_count',
//                params: {
//                    product_id: this.button.dataset.id,
//                },
//            });
//            Dialog.alert(this, 'Now you can share this content', { title: 'Copied!'  });
//        },
    });


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


//  fieldRegistry.add('qr_code', QRCode);
    registry.WidgetButton = WidgetButton;
//    console.log('is ready listo');
      console.log('CALSS BOTON');
});