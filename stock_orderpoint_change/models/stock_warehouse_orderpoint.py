# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 ICTSTUDIO (<http://www.ictstudio.eu>).
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

from openerp import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class StockWarehouseOrderpoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'

    @api.multi
    def action_cancel_chain(self):
        for rec in self:
            chained_procurements = rec.procurement_ids.get_chained_procurements()
            _logger.debug("Chained Procurements: %s", chained_procurements)
            cancel_procurements, error_procurements = chained_procurements.cancel_chain()
            if error_procurements:
                _logger.debug("Errors: %s", error_procurements)
            if cancel_procurements:
                _logger.debug("Cancel: %s", cancel_procurements)
        return True