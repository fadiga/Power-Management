#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from PyQt4 import QtGui, QtCore
from sqlalchemy import desc
from database import *
from common import PowerWidget, PowerPageTitle, PowerTableWidget
from gettext import gettext as _


class DashbordViewWidget(PowerWidget):

    def __init__(self, parent=0, *args, **kwargs):
        super(DashbordViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)
        self.title = PowerPageTitle(u"Dashbord")
        self.title_alert = PowerPageTitle(u"Alert")
        self.table_balance = BalanceTableWidget(parent=self)
        self.table_consumption = ConsumptionTableWidget(parent=self)
        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        hbox_alert = QtGui.QHBoxLayout()
        hbox_alert.addWidget(self.title_alert)
        vbox.addWidget(self.title)
        tablebox_balance = QtGui.QHBoxLayout()
        tablebox_consumption = QtGui.QHBoxLayout()
        tablebox_balance.addWidget(self.table_balance)
        tablebox_consumption.addWidget(self.table_consumption)
        hbox.addLayout(tablebox_balance)
        hbox.addLayout(tablebox_consumption)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox_alert)
        self.setLayout(vbox)


class BalanceTableWidget(PowerTableWidget):

    def __init__(self, parent, *args, **kwargs):

        PowerTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"Date"), _(u"Type"), \
                        _(u"Value")]
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        self.data = [(op.date_op.strftime(u'%d-%m-%Y %Hh:%Mmn'), op.type, op.valeur)
            for op in session.query(Operation).filter(Operation.type=='Solde').\
                      order_by(desc(Operation.date_op)).all()]


class ConsumptionTableWidget(PowerTableWidget):

    def __init__(self, parent, *args, **kwargs):

        PowerTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"Date"), _(u"Type"), \
                        _(u"Valeur")]
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        self.data = [(op.date_op.strftime(u'%d-%m-%Y %Hh:%Mmn'),\
                                                op.type, op.valeur)
            for op in session.query(Operation).all()]
