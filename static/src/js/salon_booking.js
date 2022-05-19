console.log('is ready listo');
'use strict';
//De esta forma usamos el compilador de java script de odoo
//Recibe el nombre del modulo . el nombre del java script
odoo.define('web.salon_booking', function (require) {


//    Empieza a ejecutar todo una ves que el dom este cargado
    require('web.dom_ready');
//    El ajax nos permitira hacer la conexion con controllers de odoo
    var ajax = require('web.ajax');
    var session = require('web.session');
//    var country = require("res.country");
//    var model = require('libros');


    var user = session.uid
    console.log('user >>>> ', user)


      $(document).on('click',"#submit_button",function() {

        console.log("jd");
//               Dialog.alert(
//                this,
//                'Has copiado la URL',
//                {
//                    title: 'Exito'
//                }
//             );
        data1 = {'name': 'Katty'}
        ajax.jsonRpc('/get_map', 'call', {'name':'date1', 'name1':'date2', 'user':user}).then(function(data){
            console.log(data);
        });


    });

});

function funcion1(){
    console.log('salio');
//    alert('holahhhhhhhhhhhhhh');
}
