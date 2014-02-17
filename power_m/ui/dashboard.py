#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

import os

from PyQt4 import QtGui
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
from jinja2 import Environment, PackageLoader

from utils import get_temp_filename, formatted_number
from database import Operation
from datahelper import (tabbox, consumption, duration,
                      estimated_duration, max_consumption, average_consumption,
                      last_balance, balance_graph, consumption_graph)
from common import (PowerWidget, PowerPageTitle, PowerTableWidget,
                                                PowerBoxTitle)

abs_path = os.path.abspath(__file__)
ROOT_DIR = os.path.dirname(abs_path)
BASE_URL = 'file://' + ROOT_DIR


class DashbordViewWidget(PowerWidget):
    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(DashbordViewWidget, self).__init__(parent=parent, *args, **kwargs)

        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        box_left = QtGui.QHBoxLayout()
        box_rigth = QtGui.QHBoxLayout()
        hbox_alert = QtGui.QVBoxLayout()

        box = QtGui.QListWidget()
        consuption = max_consumption()
        duration_cut = duration()
        avg_conso = average_consumption()
        num_days = estimated_duration()

        #All alerts
        if consuption:
            box.addItem(_(u"The increased consumption is %(conso)s"
                          u" cfa (%(date)s).")\
                          % {'conso': formatted_number(consuption[0]),
                          'date': consuption[1].strftime(u'%x')})
        if duration_cut:
            box.addItem(_(u"The biggest break is %(duration)s (%(date)s).")\
                                % {'duration': duration_cut[0],
                                   'date': duration_cut[1].strftime(u"%x")})
        if avg_conso:
            box.addItem(_(u"The average consumption is %(avg)s FCFA.")
                                % {'avg': formatted_number(avg_conso)})
        if num_days:
            box.addItem(_(u"The end balance is estimated at %(num)s days.")
                                % {'num': num_days})

        tablebox_balance = QtGui.QVBoxLayout()
        tablebox_consumption = QtGui.QVBoxLayout()

        # On recupere la derniere balance
        msg = _("Balance:  {} FCFA")
        balance = last_balance()
        balance = msg.format(0 if not balance else formatted_number(balance))

        self.title = PowerPageTitle(balance)
        self.title_alert = PowerPageTitle(_(u"Statistics"))
        self.title_box_balance = PowerBoxTitle(_(u"Table balances"))
        self.title_box_consumption = PowerBoxTitle(_(u"Table consumptions"))

        self.table_balance = BalanceTableWidget(parent=self)
        self.table_consumption = ConsumptionTableWidget(parent=self)

        # GRAPH
        jinja = Environment(loader=PackageLoader('power_m', 'templates'))
        template = jinja.get_template('chart.html')
        graph1 = template.render(base_url=BASE_URL, type="balance", data=balance_graph()[1],
                                 date=balance_graph()[0])
        graph2 = template.render(base_url=BASE_URL,  type="consuption", data=consumption_graph()[1],
                                 date=consumption_graph()[0])

        label_b = QWebView()
        label_b.setHtml(graph1)
        box_left.addWidget(label_b)
        label_cons = QWebView()
        label_cons.setHtml(graph2)
        box_rigth.addWidget(label_cons)

        hbox_alert.addWidget(self.title_alert)
        hbox_alert.addWidget(box)

        #Combobox widget
        list_type = [_(u"Week"), _(u"Month")]
        self.box_type = QtGui.QComboBox()
        for index in list_type:
            self.box_type.addItem((u"%(type)s") % {"type": index})

        box_combo = QtGui.QHBoxLayout()
        box_combo.addWidget(self.box_type)
        box_combo.addSpacing(930)

        vbox.addWidget(self.title)
        vbox.addLayout(box_combo)
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

        self.data = [(op.date_op.strftime(_(u'%x %Hh:%Mmn')), op.type_,
                     formatted_number(op.value), formatted_number(op.balance))
                     for op in Operation.select().order_by(('date_op', 'asc'))]


class ConsumptionTableWidget(PowerTableWidget):

    def __init__(self, parent, *args, **kwargs):

        PowerTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"Date"), _(u"Consumption")]
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        consumptions = consumption()
        consumptions.reverse()
        self.data = [(op[0].strftime(_(u'%x %Hh:%Mmn')),\
                            formatted_number(op[1]))
            for op in consumptions]
