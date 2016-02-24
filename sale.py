# This file is part of the sale_customer_reference module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Not, Equal

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'
    customer_reference = fields.Char('Customer Reference', select=True,
        states={
            'readonly': Not(Equal(Eval('state'), 'draft')),
            }, depends=['state'])

    def _get_shipment_sale(self, Shipment, key):
        shipment = super(Sale, self)._get_shipment_sale(Shipment, key)
        shipment.customer_reference = self.customer_reference
        return shipment
