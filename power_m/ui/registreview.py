#!/usr/bin/env python
# encoding=utf-8
# maintainer: Alou

from PyQt4 import QtGui
from PyQt4 import QtCore

from common import PowerWidget
# from database import Operation
from prints import build_consumption_report, build_balance_report,\
                                                    build_all_report
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
        self.data_type = [_(u"Balance"), _(u"Consumption")]

        self.box_type.addItem(_(u"All"))
        for index in xrange(0, len(self.data_type)):
            type_ = self.data_type[index]
            self.box_type.addItem(_(u'%(type)s') % {'type': type_})

        button_hbox = QtGui.QHBoxLayout()

        operation_but = QtGui.QPushButton(_("Print"))
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
        ''' Call build_operations_report '''

        index = self.box_type.currentIndex()

        if index == 0:
            pdf_report = build_all_report()
        elif index == 1:
            pdf_report = build_balance_report()
        elif index == 2:
            pdf_report = build_consumption_report()

        uopen_file(pdf_report)
