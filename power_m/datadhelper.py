#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from database import *
from datetime import date, datetime
from sqlalchemy import desc, func


def consomation(operations):
    ''' total amount expendited during that period '''
    operation_balances = session.query(Operation.valeur)
                                .filter(Operation.type=='Solde').all()

