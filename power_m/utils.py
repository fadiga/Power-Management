#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from PyQt4 import QtGui
from ui.window import PowerWindow


def raise_error(title, message):
    box = QtGui.QMessageBox(QtGui.QMessageBox.Critical, title, \
                            message, QtGui.QMessageBox.Ok, \
                            parent=PowerWindow.window)
    box.exec_()


def raise_success(title, message):
    box = QtGui.QMessageBox(QtGui.QMessageBox.Information, title, \
                            message, QtGui.QMessageBox.Ok, \
                            parent=PowerWindow.window)
    box.exec_()
