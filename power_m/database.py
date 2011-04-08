#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fad

from gettext import gettext as _
from datetime import date, datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper, relationship
from sqlalchemy import Table, Column, Integer, String, \
                       MetaData, ForeignKey, Date, DateTime, Unicode

DB_FILE = 'power.db'

engine = create_engine('sqlite:///%s' % DB_FILE, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

operations_table = Table('operation', metadata,
    Column('id', Integer, primary_key=True),
    Column('date_op', DateTime),
    Column('type', String(20)),
    Column('value', Integer),
    Column('balance', Integer),
)

metadata.create_all(engine)


class Operation(object):

    def __init__(self, date_op, type, value=0, balance=0):
        self.date_op = date_op
        self.type = type
        self.value = value
        self.balance = balance

    def __repr__(self):
        return _("<Operation('%(value)s')>") % {'value': str(self.value)}

    def __unicode__(self):
        return _(u"%(date_op)s %(type)s: %(value)s %(balance)s")\
               % {'date_op': self.date_op.strftime(u'%d-%m-%Y %Hh:%Mmn'),\
                  'type': self.type,\
                  'value': self.value, 'balance': self.balance}

mapper(Operation, operations_table)
