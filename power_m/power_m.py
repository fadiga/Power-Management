#!/usr/bin/env python
#encoding = utf-8
#maintainer : Fad

import sys

from PyQt4 import QtCore, QtGui

from ui.mainwindow import MainWindows


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    qb = MainWindows()
    qb.show()
    sys.exit(app.exec_())
