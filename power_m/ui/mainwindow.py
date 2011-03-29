#!usr/bin/env python
# encoding=utf-8
# maintainer: Fad


import sys
from PyQt4 import QtCore, QtGui
from menubar import MenuBar


class MainWindows(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setGeometry(0, 30, 900, 650)
        self.setWindowTitle('Prower Management')
        self.setWindowIcon(QtGui.QIcon('icons/fad.png'))
        self.menubar = MenuBar(self)
        self.setMenuBar(self.menubar)

    def change_context(self, context_widget, *args, **kwargs):

        # instanciate context
        self.view_widget = context_widget(parent=self, *args, **kwargs)

        # refresh menubar
        self.menubar.refresh()

        # attach context to window
        self.setCentralWidget(self.view_widget)
