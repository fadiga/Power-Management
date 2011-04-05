#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou
from PyQt4 import QtGui
from database import *
from datetime import date, datetime
from sqlalchemy import desc, func
from ui.common import TabPane


def tabbox(box1, Box2):
    ''' adds a box with tab '''
    tab_widget = QtGui.QTabWidget()
    for heading in ["Graphe", "Table"]:
            pane = TabPane()
            if heading == "Graphe":
                pane.addBox(box1)
            else:
                pane.addBox(Box2)
            tab_widget.addTab(pane, heading)
    return tab_widget
