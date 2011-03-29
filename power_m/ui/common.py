#!/usr/bin/env python
# encoding=utf-8
# maintainer: alou


from PyQt4 import QtGui
from PyQt4.QtCore import Qt
MAIN_WIDGET_SIZE = 900

class PowerPageTitle(QtGui.QLabel):

    def __init__(self, *args, **kwargs):
        super(PowerPageTitle, self).__init__(*args, **kwargs)
        self.setFont(QtGui.QFont("Times New Roman", 18))
        self.setAlignment(Qt.AlignCenter)

class PowerWidget(QtGui.QWidget):

    def __init__(self, parent=0, *args, **kwargs):

        QtGui.QWidget.__init__(self, parent=parent, *args, **kwargs)

        self.setMaximumWidth(MAIN_WIDGET_SIZE)

    def refresh(self):
        pass

    def change_main_context(self, context_widget, *args, **kwargs):
        return self.parentWidget()\
                          .change_context(context_widget, *args, **kwargs)

    def open_dialog(self, dialog, modal=False, *args, **kwargs):
        return self.parentWidget().open_dialog(dialog, \
                                               modal=modal, *args, **kwargs)
