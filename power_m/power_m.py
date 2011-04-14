#!/usr/bin/env python
#encoding = utf-8
#maintainer : Fad

import sys
import gettext
import locale

from PyQt4 import QtCore, QtGui
import gettext_windows
from ui.mainwindow import MainWindows


def main():
    gettext_windows.setup_env()

    locale.setlocale(locale.LC_ALL, '')

    gettext.install('power_m', localedir='locale', unicode=True)

    app = QtGui.QApplication(sys.argv)
    qb = MainWindows()
    qb.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

