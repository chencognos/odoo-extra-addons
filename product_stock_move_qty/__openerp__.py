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
    'name': 'Product Stock Move Qty',
    'version': '8.0.1.1.3',
    'website': 'http://www.ictstudio.eu',
    'category': 'Product',
    'summary': 'Show Product Stock Moves Qty for Location/Warehouse',
    'description': """
Product Stock Move Qty
===========================
- Show Product Stock Moves Qty for Location/Warehouse
""",
    'author': 'ICTSTUDIO, André Schenkels',
    'depends': ['stock'],
    'data': [
        # 'security/product_marker_security.xml',
        'views/stock_move_location.xml',
        'views/product_template.xml',
        'views/product_product.xml',
        # 'security/ir.model.access.csv',
    ],
}

