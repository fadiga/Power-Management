#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from PyQt4 import QtGui, QtCore
from database import *
from common import PowerWidget, PowerPageTitle

class DashbordViewWidget(PowerWidget):
    def __init__(self, parent=0, *args, **kwargs):
        super(DashbordViewWidget, self).__init__(parent=parent, *args, **kwargs)
        self.title = PowerPageTitle(u"Dashbord")

        vbox = QtGui.QVBoxLayout()

        vbox.addWidget(self.title)
        self.setLayout(vbox)
