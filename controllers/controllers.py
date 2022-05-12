# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

class OdooContr4ollers(http.Controller):
	# La ruta ni la funcion se puede repetir dentro de esta clase podemos tener muchas pero solo un "get_products"
	# type = 'json' TANTO LA CONXION COMO LA DEVOLUCION NOS DEVOLVERA JSON
	# auth = 'public' SI NO LE PONES PUBLIC TENDRAS QUE PONER USER, CONTRASEÑA
	# sudo() SOLO LA LINEA DE CODIGO TENDRA ACCESO DE SUPER USUARIO
	@http.route(['/get_products'], type='json', auth='public',  website=True)
	def get_products(self, **post):
		name = post.get('name', False)
		name1 = post.get('name1', False)

		print(name+ '---------'+ name1)
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
		print(p)


		return p

	@http.route('/create_employee', type='json', auth='public', method=['POST'], cors='*', csrf=False)
	def create_employee(self, **post):
		# Create Home Address
		home_address = request.env['res.partner'].sudo().create({
			'name': 'CRC25',
			'zip': '201301',
			'phone': '99999999',
			'email': 'email@email.com',
		})
		print(home_address)
		print('FIN')
