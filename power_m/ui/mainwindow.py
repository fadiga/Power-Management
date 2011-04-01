#!usr/bin/env python
# encoding=utf-8
# maintainer: Fad


import sys
from PyQt4 import QtCore, QtGui
from menubar import MenuBar
from dashbord import DashbordViewWidget


class MainWindows(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setGeometry(0, 30, 900, 650)
        self.setWindowTitle('Prower Management')
        self.setWindowIcon(QtGui.QIcon('icons/power-icon.png'))
        self.menubar = MenuBar(self)
        self.setMenuBar(self.menubar)
        self.change_context(DashbordViewWidget)

    def change_context(self, context_widget, *args, **kwargs):

        # instanciate context
        self.view_widget = context_widget(parent=self, *args, **kwargs)

        # refresh menubar
        self.menubar.refresh()

        # attach context to window
        self.setCentralWidget(self.view_widget)

    def open_dialog(self, dialog, modal=False, *args, **kwargs):
        d = dialog(parent=self, *args, **kwargs)
        d.setModal(modal)
        d.exec_()
