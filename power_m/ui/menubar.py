#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from PyQt4 import QtGui, QtCore

from exports import export_database_as_file
from dashboard import DashbordViewWidget
from common import PowerWidget
from statementview import AddstatementViewWidget
from registreview import RegistreWidget
from deleteview import DeleteViewWidget


class MenuBar(QtGui.QMenuBar, PowerWidget):

    def __init__(self, parent=None, *args, **kwargs):
        QtGui.QMenuBar.__init__(self, parent, *args, **kwargs)

        # change icon so that it appears in About box
        self.setWindowIcon(QtGui.QIcon('images/yeleman_logo.png'))

        #Menu File
        file = self.addMenu(_(u"&File"))
        # Delete
        self.delete = QtGui.QAction(_(u"Delete a statement"), self)
        self.connect(self.delete, QtCore.SIGNAL("triggered()"),\
                                            self.goto_delete_statement)
        self.delete.setEnabled(True)
        file.addAction(self.delete)

        # Print
        print_statement = QtGui.QAction(_(u"Print"), self)
        print_statement.setShortcut("Ctrl+P")
        self.connect(print_statement, QtCore.SIGNAL("triggered()"),\
                                            self.goto_print)
        file.addAction(print_statement)
        # Export
        export = file.addMenu(_(u"&Export data"))
        export.addAction(_(u"Backup Database"), self.goto_export_db)

        # Exit
        exit = QtGui.QAction(_(u"Exit"), self)
        exit.setShortcut("Ctrl+Q")
        exit.setToolTip(_("Exit application"))
        self.connect(exit, QtCore.SIGNAL("triggered()"), \
                                         self.parentWidget(), \
                                         QtCore.SLOT("close()"))
        file.addAction(exit)
        # Menu go to
        goto = self.addMenu(_(u"&Go to"))
        goto.addAction(_(u"Dashboard"),\
                                    self.goto_dashbord)
        goto.addAction(_(u"Add Statement"),\
                                       self.goto_add_statement)
        #Menu help
        help = self.addMenu(_(u"Help"))
        help.addAction(_(u"About"), self.goto_about)

    #Print
    def goto_print(self):
        self.open_dialog(RegistreWidget, modal=True)

    def goto_add_statement(self):
        self.open_dialog(AddstatementViewWidget, modal=True)

    #Delete an operation.
    def goto_delete_statement(self):
        self.open_dialog(DeleteViewWidget, modal=True)

    #Export the database.
    def goto_export_db(self):
        export_database_as_file()

    # dashbord
    def goto_dashbord(self):
        self.change_main_context(DashbordViewWidget)

    #About
    def goto_about(self):
        mbox = QtGui.QMessageBox.about(self, _(u"About Power-M"), \
                          _(u"Power-M Power Management Software\n\n" \
                            u"© 2011 yɛlɛman s.à.r.l\n" \
                            u"Hippodrome, Avenue Al Quds, \n" \
                            u"BPE. 3713 - Bamako (Mali)\n" \
                            u"Tel: (223) 76 33 30 05\n" \
                            u"www.yeleman.com\n" \
                            u"info@yeleman.com\n\n" \
                            u"Alou Dolo, Ibrahima Fadiga, \n"))
