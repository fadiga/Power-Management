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

engine = create_engine('sqlite:///%s' % DB_FILE, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

operations_table = Table('operation', metadata,
    Column('id', Integer, primary_key=True),
    Column('date_op', Date),
    Column('type', String(20)),
    Column('valeur', Integer),
)

metadata.create_all(engine)


class Operation(object):

    def __init__(self, date_op, type, valeur=0):
        self.date_op = date_op
        self.type = type
        self.valeur = valeur

    def __repr__(self):
        return _("<Operation('%(valeur)s')>") % {'valeur': str(self.valeur)}

    def __unicode__(self):
        return _(u"%(date_op)s %(type)s: %(valeur)s") \
               % {'date_op': self.date_op.strftime('%F'), \
                  'type': self.type, \
                  'valeur': self.valeur}

mapper(Operation, operations_table)


