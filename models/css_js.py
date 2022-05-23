# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class css_js(models.Model): 
    _name = 'ej.css_js'
    marker_color = fields.Char(
        string='Marker Color', default='red', required=True)

    Ventas = fields.Char(string='Venta')
    valor = fields.Char(string='Bandera')
    user = fields.Char(string='Usuario')

    field_one = fields.Integer('Field One', default=1)
    field_two = fields.Integer('Field Two')
    field_three = fields.Integer('Field Three')

    is_check = fields.Boolean(string="Bandera", default=False);
    posicion = fields.Char(string='Posicion')

    @api.model
    def your_function(self):
        # CODE TO GET VALUE
        print('hola')
        return 'Hola'


    def write(self, values):
        """Override default Odoo write function and extend."""
        # Do your custom logic here
        print('GUARDAR')
        record_ids = self.env['ej.css_js'].search([('is_check', '=', True), ('user', '=', self.env.uid)],  limit=1, order='id desc')
        print(record_ids)
        for record in record_ids:
            # record.write({
            #     'is_check': False
            # })
            print(record.Ventas)
            values['is_check'] = False
            values['posicion']= record.valor
        # ELIMINAR REGISTROS DE LA BD
        self.env['ej.css_js'].search([('is_check', '=', True), ('user', '=', self.env.uid)], limit=100, order='id desc').unlink()
        return super(css_js, self).write(values)

    @api.model
    def create(self, values):
        """Override default Odoo create function and extend."""
        # Do your custom logic here
        print('CREAR')
        # record = self.env['your.model'].create({
        #     'name': 'Example'
        # })
        print(self.is_check)
        return super(css_js, self).create(values)


    def action_url(sel):
        print('URL')
        # return {
        #     'type': 'ir.actions.act_url',
        #     'target': 'self',
        #     'url': '/web#action=666&active_id=12&model=res.partner&view_type=google_map&cids=&menu_id=202',
        # }

        # usar % self.user
        id= '13'
        url = '/web#action=666&active_id='+id+'&model=res.partner&view_type=google_map&cids=&menu_id=202'
        print(url)
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': url,
        }