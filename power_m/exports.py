#!/usr/bin/env python
# encoding=utf-8
# maintainer: alou


import os
import shutil
from datetime import datetime

from PyQt4 import QtGui

import database
from database import Operation
from utils import raise_success, raise_error


def export_database_as_file():
    destination = QtGui.QFileDialog.getSaveFileName(QtGui.QWidget(), \
                                    _(u"Save DB as..."), \
                                    "%s.db" % datetime.now()\
                                                .strftime('%d-%m-%Y %Hh%M'), \
                                    "*.db")
    if not destination:
        return

    try:
        shutil.copyfile(database.DB_FILE, destination)
        raise_success(_(u"Database exported!"), \
                      _(u"The Database has been successfuly exported.\n" \
                        u"Keep that file private as it contains your data.\n" \
                        u"Export your data regularly."))
    except IOError:
        raise_error(_(u"Error in exporting Database!"), \
                    _(u"The database backup could not be exported.\n" \
                      u"Please verify that you selected a destination " \
                      u"folder which you have write permissions to.\n" \
                      u"Then retry.\n\n" \
                      u"Request assistance if the problem persist."))
