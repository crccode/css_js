# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) CRC 
#    (<http://www.myweb.cl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'css_js CRC',
    'version': '14.0.1.0',
    'author': "CRC",
    'maintainer': 'Ynext',
    'website': 'http://www.crc.cl',
    'license': 'AGPL-3',
    'category': 'account.payment',
    'summary': 'Ejemplo de un m�dulo by Ynext.',
    'depends': ['base','stock'],
    'description': """
Modulo basado en Ynext
===================================================== 
�ste m�dulo permite selecionar 
""",
    'demo': [],
    'test': [],
    'data': ['views/css_js_view.xml','views/js_view.xml', 'security/ir.model.access.csv'],
    'installable': True,
    'auto_install': False,
}
