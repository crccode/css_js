# -*- coding: utf-8 -*-
import json
from datetime import datetime, date
from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

class OdooContr4ollers(http.Controller):
	# La ruta ni la funcion se puede repetir dentro de esta clase podemos tener muchas pero solo un "get_products"
	# public Para que podamos acceder sin registrarno
	@http.route(['/get_products'], type='json', auth='public',  website=True)
	def get_products(self, **post):
		print('python')
		products = http.request.env['product.product'].sudo().search([('active', '=', True)], limit=6)
		print(products)
		p= []
		for product in products:
			n= {
				"name": product.default_code,
				"id": product.id
			}
			p.append(n)
		return p

