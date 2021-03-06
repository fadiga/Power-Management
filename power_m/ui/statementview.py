#!usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer: Fad


from datetime import datetime

from PyQt4 import QtGui, QtCore

from database import Operation
from dashboard import DashbordViewWidget
from common import PowerWidget, PowerPageTitle
from datahelper import last_balance
from utils import raise_success, raise_error


class AddstatementViewWidget(QtGui.QDialog, PowerWidget):

    def __init__(self, parent=0, *args, **kwargs):
        QtGui.QDialog.__init__(self, parent, *args, **kwargs)
        self.setWindowTitle(_(u"Add statement"))
        self.title = PowerPageTitle(_(u"statement"))

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title)

        titelebox = QtGui.QGridLayout()
        titelebox.addWidget(QtGui.QLabel((_(u"   Date"))), 0, 1)
        titelebox.addWidget(QtGui.QLabel((_(u"    Time"))), 0, 2)
        titelebox.addWidget(QtGui.QLabel((_(u"Type"))), 0, 3)
        titelebox.addWidget(QtGui.QLabel((_(u"Value"))), 0, 4)
        vbox.addLayout(titelebox)

        self.list_data = []
        for n in range(0, 5):
            self.date_ = QtGui.QDateTimeEdit(QtCore.QDate.currentDate())
            self.date_.setDisplayFormat("dd/MM/yyyy")
            self.time = QtGui.QDateTimeEdit(QtCore.QTime.currentTime())
            self.time.setDisplayFormat("hh:mm")
            self.type_ = QtGui.QLineEdit()
            self.value_ = QtGui.QLineEdit()
            self.value_.setValidator(QtGui.QIntValidator())

            liste_type = [_("balance"), _("added"), _("cut"), _("recovery")]
            #Combobox widget
            self.box_type = QtGui.QComboBox()
            for index in liste_type:
                self.box_type.addItem(u'%(type)s' % {'type': index})

            self.list_data.append((self.date_, self.time,
                                   self.box_type, self.value_))

            editbox = QtGui.QHBoxLayout()
            editbox.addWidget(self.date_)
            editbox.addWidget(self.time)
            editbox.addWidget(self.box_type)
            editbox.addWidget(self.value_)
            vbox.addLayout(editbox)

        button_hbox = QtGui.QHBoxLayout()
        butt = QtGui.QPushButton(_(u"Add"))
        butt.clicked.connect(self.add_statement)
        cancel_but = QtGui.QPushButton(_(u"Cancel"))
        cancel_but.clicked.connect(self.cancel)
        button_hbox.addWidget(cancel_but)
        button_hbox.addWidget(butt)

        vbox.addLayout(button_hbox)
        self.setLayout(vbox)

    def cancel(self):
        self.close()

    def add_statement(self):
        ''' add statement '''
        types = {0: "balance", 1: "added", 2: "cut", 3: "recovery"}
        commit = False
        for data in self.list_data:
            date_op = data[0].text()
            time_op = data[1].text()
            type_op = types[data[2].currentIndex()]
            value_op = data[3].text()

            day, month, year = date_op.split('/')
            hour, minute = time_op.split(':')
            datetime_ = datetime(int(year), int(month),
                                 int(day), int(hour), int(minute))
            flag = False
            last_b = last_balance()
            if value_op:
                flag = True
            if type_op == "recovery" or type_op == "cut":
                flag = True
            if flag:
                if type_op == "added":
                    if last_b == None:
                        balance = int(value_op)
                    else:
                        balance = int(last_b) + int(value_op)
                if type_op == "balance":
                    balance = unicode(value_op)
                if type_op == "recovery" or type_op == "cut":
                    balance = unicode(last_b)

                try:
                    operation = Operation.create(date_op=datetime_, type_=unicode(type_op),
                                      value=unicode(value_op), balance=balance)
                    raise_success(_(u"Confirmation"), _(u"Registered opération"))
                except:
                    raise
                    raise_error(_(u"Confirmation"), _(u"There is no valid operation"))
        self.change_main_context(DashbordViewWidget)
