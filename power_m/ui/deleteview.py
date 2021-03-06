#!/usr/bin/env python
# encoding=utf-8
# maintainer: alou

from PyQt4 import QtGui
from PyQt4 import QtCore

from utils import raise_error, raise_success, formatted_number
from common import PowerWidget
from database import Operation
from dashboard import DashbordViewWidget


class DeleteViewWidget(QtGui.QDialog, PowerWidget):

    def __init__(self, parent, *args, **kwargs):
        QtGui.QDialog.__init__(self, parent, *args, **kwargs)

        self.data = Operation.select().order_by("date_op")

        title = QtGui.QLabel()
        self.setWindowTitle(_(u"Delete an operation"))
        if self.data == []:
            title.setText(_(u"There is no operation removed for this account"))
            ok_butt = QtGui.QPushButton(_(u"OK"))
            ok_butt.clicked.connect(self.close)

            vbox = QtGui.QVBoxLayout()
            vbox.addWidget(title)
            vbox.addWidget(ok_butt)
            self.setLayout(vbox)
        else:
            title.setText(_(u"Select a statement has deleted"))
            title.setAlignment(QtCore.Qt.AlignHCenter)
            title_hbox = QtGui.QHBoxLayout()
            title_hbox.addWidget(title)

            #Combobox widget
            # self.box = QtGui.QComboBox()
            # for index in xrange(0, self.data.count()):
            #     op = self.data[index]
            #     sentence = _(u"%(date_op)s - %(type)s - " \
            #                  u"%(value)s/%(balance)s ")\
            #                  % {'date_op': op.date_op, \
            #                     'type': op.type, \
            #                     'value': op.value, \
            #                     'balance': formatted_number(op.balance)}
            #     self.box.addItem(sentence, QtCore.QVariant(op.id))
            self.box = QtGui.QComboBox()
            for index in self.data:
                op = index
                sentence = _(u"%(date_op)s - %(type)s - " \
                             u"%(value)s/%(balance)s ")\
                             % {'date_op': op.date_op, \
                                'type': op.type_, \
                                'value': op.value, \
                                'balance': formatted_number(op.balance)}
                self.box.addItem(sentence, QtCore.QVariant(op.id))

            combo_hbox = QtGui.QHBoxLayout()
            combo_hbox.addWidget(self.box)

            #delete and cancel hbox
            button_hbox = QtGui.QHBoxLayout()

            #Delete Button widget.
            delete_but = QtGui.QPushButton(_(u"Delete"))
            delete_but.clicked.connect(self.delete)
            #Cancel Button widget.
            cancel_but = QtGui.QPushButton(_(u"Cancel"))
            cancel_but.clicked.connect(self.cancel)

            button_hbox.addWidget(cancel_but)
            button_hbox.addWidget(delete_but)
            #Create the QVBoxLayout contenaire.
            vbox = QtGui.QVBoxLayout()
            vbox.addLayout(title_hbox)
            vbox.addLayout(combo_hbox)
            vbox.addLayout(button_hbox)
            self.setLayout(vbox)

    def cancel(self):
        self.close()

    def delete(self):
        op = self.data[self.box.currentIndex()]
        op.delete_instance()
        self.change_main_context(DashbordViewWidget)
        self.box.removeItem(self.box.currentIndex())
        if len(self.data) == 1:
            self.close()
        else:
            self.data.pop(self.box.currentIndex())
        raise_success(_(u"Deleting"), _(u"Operation succefully removed"))
