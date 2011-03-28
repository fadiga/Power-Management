#!usr/bin/env python
# encoding=utf-8
# maintainer: Fad


import sys
from PyQt4 import QtCore, QtGui


class MainWindows(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setGeometry(0, 30, 1200, 680)
        self.setWindowTitle('Prower Management')
        self.setWindowIcon(QtGui.QIcon('icons/fad.png'))

