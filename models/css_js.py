# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class css_js(models.Model): 
    _name = 'ej.css_js' 
    Ventas = fields.Char(string='Venta')
 
