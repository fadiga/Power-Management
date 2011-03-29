#!usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer: Fad


from datetime import datetime

from PyQt4 import QtGui, QtCore
from database import *

from common import PowerWidget, PowerPageTitle


class AddstatementViewWidget(QtGui.QDialog, PowerWidget):

    def __init__(self, parent=0, *args, **kwargs):
        super(AddstatementViewWidget, self).__init__(parent=parent, *args,\
                                                                **kwargs)
        self.title = PowerPageTitle(u"statement")

        formbox = QtGui.QFormLayout()
        self.date_ = QtGui.QDateTimeEdit(QtCore.QDate.currentDate())
        self.date_.setDisplayFormat("yyyy-MM-dd")
        self.type_ = QtGui.QLineEdit()
        self.value_ = QtGui.QLineEdit()
        self.value_.setValidator(QtGui.QIntValidator())

        #~ self.label.move(130, 100)
        titelebox = QtGui.QHBoxLayout()
        titelebox.addWidget(QtGui.QLabel((u'Date')))
        titelebox.addWidget(QtGui.QLabel((u'Type')))
        titelebox.addWidget(QtGui.QLabel((u'Value')))

        editbox = QtGui.QHBoxLayout()
        editbox.addWidget(self.date_)
        editbox.addWidget(self.type_)
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
        date_ = datetime(int(year), int(month), int(day))

        if self.date_ and self.type_ and self.value_:
            operation = Operation(date_, unicode(self.type_.text()),\
                            unicode(self.value_.text()))
            session.add(operation)
            session.commit()
