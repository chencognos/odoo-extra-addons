# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 ICTSTUDIO (<http://www.ictstudio.eu>).
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
    'name': 'Selective Picking Return',
    'version': '8.0.0.0.2',
    'author': 'ICTSTUDIO, André Schenkels',
    'category': 'Stock Management',
    'website': 'https://www.odoo.com',
    'depends': ['stock'],
    'demo': [],
    'summary': "Selective Picking Returns",
    'data': [
        'wizard/stock_picking_return.xml',
        'wizard/stock_picking_return_line.xml',
        'views/stock_picking.xml',
    ],
}

