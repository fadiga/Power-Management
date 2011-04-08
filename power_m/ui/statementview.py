#!usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer: Fad


from datetime import datetime

from PyQt4 import QtGui, QtCore

from database import *
from dashboard import DashbordViewWidget
from common import PowerWidget, PowerPageTitle
from datahelper import last_balance

class AddstatementViewWidget(QtGui.QDialog, PowerWidget):

    def __init__(self, parent=0, *args, **kwargs):
        QtGui.QDialog.__init__(self, parent, *args, **kwargs)
        self.title = PowerPageTitle(u"statement")

        formbox = QtGui.QFormLayout()
        self.date_ = QtGui.QDateTimeEdit(QtCore.QDate.currentDate())
        self.date_.setDisplayFormat("yyyy-MM-dd ")
        self.time = QtGui.QDateTimeEdit(QtCore.QTime.currentTime())
        self.time.setDisplayFormat("hh:mm")
        self.type_ = QtGui.QLineEdit()
        self.value_ = QtGui.QLineEdit()
        self.value_.setValidator(QtGui.QIntValidator())

        #~ self.label.move(130, 100)
        titelebox = QtGui.QHBoxLayout()
        titelebox.addWidget(QtGui.QLabel((u'Date')))
        titelebox.addWidget(QtGui.QLabel((u'time')))
        titelebox.addWidget(QtGui.QLabel((u'Type')))
        titelebox.addWidget(QtGui.QLabel((u'Value')))

        liste_type = ["Solde", "Ajout", "Coupure", "Reprise"]
        #Combobox widget
        self.box_type = QtGui.QComboBox()
        for index in liste_type:
            self.box_type.addItem((u'%(type)s') % {'type': index})

        editbox = QtGui.QHBoxLayout()
        editbox.addWidget(self.date_)
        editbox.addWidget(self.time)
        editbox.addWidget(self.box_type)
        editbox.addWidget(self.value_)

        button_hbox = QtGui.QHBoxLayout()
        butt = QtGui.QPushButton((u"Add"))
        butt.clicked.connect(self.add_statement)
        cancel_but = QtGui.QPushButton((u"Cancel"))
        cancel_but.clicked.connect(self.cancel)
        button_hbox.addWidget(butt)
        button_hbox.addWidget(cancel_but)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title)

        vbox.addLayout(titelebox)
        vbox.addLayout(formbox)
        vbox.addLayout(editbox)
        vbox.addLayout(button_hbox)
        self.setLayout(vbox)

    def cancel(self):
        self.close()

    def add_statement(self):
        ''' add statement '''
        year, month, day = self.date_.text().split('-')
        hour, minute = self.time.text().split(':')
        datetime_ = datetime(int(year), int(month),\
                                int(day), int(hour),\
                                        int(minute))
        if self.date_ and self.time and self.type_ and self.value_:

            dic = {0: "Solde", 1: "Ajout", 2: "Coupure", 3: "Reprise"}
            if dic[self.box_type.currentIndex()] == "Ajout":
                balance = int(last_balance()) + int(self.value_.text())
            else :
                balance = unicode(self.value_.text())

            operation = Operation(datetime_, \
                            unicode(dic[self.box_type.currentIndex()]),\
                            unicode(self.value_.text()), balance)
            session.add(operation)
            session.commit()
            self.value_.clear()
            self.change_main_context(DashbordViewWidget)
