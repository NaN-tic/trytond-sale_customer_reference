#This file is part of the sale_customer_reference module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.

from trytond.pool import Pool
from .sale import *
from .shipment import *


def register():
    Pool.register(
        Sale,
        ShipmentOut,
        ShipmentOutReturn,
        module='sale_customer_reference', type_='model')
