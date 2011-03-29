#!usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer: Fad


from PyQt4 import QtGui, QtCore
from database import *
from common import PowerWidget, PowerPageTitle

class AddstatementViewWidget(PowerWidget):
    def __init__(self, parent=0, *args, **kwargs):
        super(AddstatementViewWidget, self).__init__(parent=parent, *args, **kwargs)
        self.title = PowerPageTitle(u"statement")

        vbox = QtGui.QVBoxLayout()

        self.label = QtGui.QLineEdit(self)
        self.label.move(130, 100)
        self.label1 = QtGui.QLineEdit(self)
        self.label1.move(130, 150)
        self.label2 = QtGui.QLineEdit(self)
        self.label2.move(130, 200)
        
        vbox.addWidget(self.title)
        vbox.addWidget(self.label)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        self.setLayout(vbox)        
        print 'zefrzdf'
