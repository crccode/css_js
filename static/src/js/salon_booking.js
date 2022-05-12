

'use strict';
odoo.define('web.salon_booking', function (require) {
    require('web.dom_ready');
    var ajax = require('web.ajax');


     $(document).on('click',"#submit_button",function() {
        console.log("jd");
        ajax.jsonRpc('/get_products', 'call', {}).then(function(data){
            console.log(data);
        });


    });

});

function funcion1(){
    console.log('salio');
//    alert('holahhhhhhhhhhhhhh');
}
