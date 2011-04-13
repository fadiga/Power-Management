#!/usr/bin/env python
# encoding=utf-8
# maintainer: Alou

from gettext import gettext as _
from PyQt4 import QtGui
from PyQt4 import QtCore

from common import PowerWidget
from database import Operation, session
from prints import build_operations_report
from utils import uopen_file


class RegistreWidget(QtGui.QDialog, PowerWidget):

    def __init__(self, parent=0, *args, **kwargs):
        QtGui.QWidget.__init__(self, parent, *args, **kwargs)

        self.setWindowTitle(_(u"Choice of type"))

        #Title widget
        title = QtGui.QLabel()
        title.setText(_(u"Choose a type"))
        title.setAlignment(QtCore.Qt.AlignHCenter)
        title_hbox = QtGui.QHBoxLayout()
        title_hbox.addWidget(title)

        #Combobox widget
        self.box_type = QtGui.QComboBox()

        #data
        self.data_type = ['Balance', 'Consumption']

        self.box_type.addItem(_(u"All Type"))
        for index in xrange(0, len(self.data_type)):
            type_ = self.data_type[index]
            self.box_type.addItem(_(u'%(type)s') % {'type': type_})

        button_hbox = QtGui.QHBoxLayout()

        operation_but = QtGui.QPushButton(_("list of operations per type"))
        button_hbox.addWidget(operation_but)
        operation_but.clicked.connect(self.operation_pdf)

        combo_hbox = QtGui.QHBoxLayout()
        combo_hbox.addWidget(self.box_type)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(title_hbox)
        vbox.addLayout(combo_hbox)
        vbox.addLayout(button_hbox)
        self.setLayout(vbox)

    def operation_pdf(self):
        """ Call build_operations_report """
        index = self.box_type.currentIndex()
        if index == 1:
            type_='Balance'
        elif index == 2:
            type_ = 'Consumption'
        else:
            type_ = 'All type'

        pdf_report = build_operations_report(type_)
        uopen_file(pdf_report)
