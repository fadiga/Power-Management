#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from PyQt4 import QtGui
from sqlalchemy import desc
from gettext import gettext as _

from database import Operation, session
from datahelper import (tabbox, graph_for_type, consumption,
                                    max_consumption, duration)
from common import (PowerWidget, PowerPageTitle, PowerTableWidget,
                                                    PowerBoxTitle)


class DashbordViewWidget(PowerWidget):

    def __init__(self, parent=0, *args, **kwargs):
        super(DashbordViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)

        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        box_left = QtGui.QHBoxLayout()
        box_rigth = QtGui.QHBoxLayout()
        hbox_alert = QtGui.QVBoxLayout()

        box = QtGui.QListWidget()
        consuption = max_consumption()
        duration_cut = duration()
        if consuption:
            box.addItem(u'The increased consumption is %s cfa (%s).'\
                                        % (consuption[1], consuption[0]))
        if duration_cut:
            box.addItem(u'The biggest break is %s (%s).'\
                                % (duration_cut[0], duration_cut[1]))

        tablebox_balance = QtGui.QVBoxLayout()
        tablebox_consumption = QtGui.QVBoxLayout()

        self.title = PowerPageTitle(u"Dashboard")
        self.title_alert = PowerPageTitle(u"Alert")
        self.title_box_balance = PowerBoxTitle(u"Table balances")
        self.title_box_consumption = PowerBoxTitle(u"Table consumptions")

        self.table_balance = BalanceTableWidget(parent=self)
        self.table_consumption = ConsumptionTableWidget(parent=self)

        pixmap = QtGui.QPixmap("graph.png")
        label = QtGui.QLabel()
        label.setPixmap(pixmap)
        graph_for_type('Representation graphique du solde par jour', 'Solde')
        box_left.addWidget(label)

        hbox_alert.addWidget(self.title_alert)
        hbox_alert.addWidget(box)

        vbox.addWidget(self.title)
        tablebox_balance.addWidget(self.title_box_balance)
        tablebox_balance.addWidget(self.table_balance)
        tablebox_consumption.addWidget(self.title_box_consumption)
        tablebox_consumption.addWidget(self.table_consumption)
        tab_widget1 = tabbox(box_left, tablebox_balance)
        tab_widget2 = tabbox(box_rigth, tablebox_consumption)

        hbox.addWidget(tab_widget1)
        hbox.addWidget(tab_widget2)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox_alert)

        self.setLayout(vbox)


class BalanceTableWidget(PowerTableWidget):

    def __init__(self, parent, *args, **kwargs):

        PowerTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"Date"), _(u"Type"), \
                        _(u"Value"), _(u"Balance")]
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        self.data = [(op.date_op.strftime(u'%d-%m-%Y %Hh:%Mmn'),\
                      op.type, op.value, op.balance)
            for op in session.query(Operation)\
                             .order_by(desc(Operation.date_op)).all()]


class ConsumptionTableWidget(PowerTableWidget):

    def __init__(self, parent, *args, **kwargs):

        PowerTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"Date"), _(u"Consumption")]
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):

        self.data = self.data = [(op[0], op[1])
            for op in consumption()]
