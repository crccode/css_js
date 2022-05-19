# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json
import logging
_logger = logging.getLogger(__name__)

class OdooContr4ollers(http.Controller):
	# La ruta ni la funcion se puede repetir dentro de esta clase podemos tener muchas pero solo un "get_products"
	# type = 'json' TANTO LA CONXION COMO LA DEVOLUCION NOS DEVOLVERA JSON
	# auth = 'public' SI NO LE PONES PUBLIC TENDRAS QUE PONER USER, CONTRASEÑA
	# sudo() SOLO LA LINEA DE CODIGO TENDRA ACCESO DE SUPER USUARIO
	@http.route(['/get_map'], type='json', auth='public', website=True)
	def get_map(self, **post):
		name, name1, user = post.get('name', False), post.get('name1', False), post.get('user', False)
		print(user)
		request.env['ej.css_js'].sudo().create({
			'valor': name+','+name1,
			'user': user,

		})


	@http.route(['/get_products'], type='json', auth='public',  website=True)
	def get_products(self, **post):
		name, name1 = post.get('name', False), post.get('name1', False)


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

	@http.route('/update_employee', type='json', auth='public', method=['POST'], cors='*', csrf=False)
	def update_employee(self, **post):
		data = json.loads(request.httprequest.data)
		email= data.get('params').get('name')
		print(data)
		print(data.get('params').get('name'))
		employee = request.env['hr.employee'].sudo().search([('work_email', '=', email)])
		if employee:
			return {'message': 'already exists'}
		else:
			id = request.env['res.partner'].sudo().create({
				'name': 'CRC25',
				'zip': '201301',
				'phone': '99999999',
				'email': 'email@email.com',
			}).id
			print(id)
			# request.env['res.partner'].sudo().
			return {'message': 'Employee {} created'.format(id)}





