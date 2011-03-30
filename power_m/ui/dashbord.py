#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from PyQt4 import QtGui, QtCore
from database import *
from common import PowerWidget, PowerPageTitle, PowerTableWidget
from gettext import gettext as _


class DashbordViewWidget(PowerWidget):
    def __init__(self, parent=0, *args, **kwargs):
        super(DashbordViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)
        self.title = PowerPageTitle(u"Dashbord")
        self.table1 = SoldeTableWidget(parent=self)
        self.table2 = ConsomationTableWidget(parent=self)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title)
        tablebox1 = QtGui.QHBoxLayout()
        tablebox2 = QtGui.QHBoxLayout()
        tablebox1.addWidget(self.table1)
        tablebox2.addWidget(self.table2)
        vbox.addLayout(tablebox1)
        vbox.addLayout(tablebox2)
        self.setLayout(vbox)


class SoldeTableWidget(PowerTableWidget):

    def __init__(self, parent, *args, **kwargs):

        PowerTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"Date"), _(u"Type"), \
                        _(u"Valeur")]
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        self.data = [(op.date_op.strftime(u'%d-%m-%Y'), op.type, op.valeur)
            for op in session.query(Operation).all()]


class ConsomationTableWidget(PowerTableWidget):

    def __init__(self, parent, *args, **kwargs):

        PowerTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"Date"), _(u"Type"), \
                        _(u"Valeur")]
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        self.data = [(op.date_op.strftime(u'%d-%m-%Y'), op.type, op.valeur)
            for op in session.query(Operation).all()]
