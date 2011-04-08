#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou
from PyQt4 import QtGui
from database import *
from datetime import date, datetime
from sqlalchemy import desc, func
from ui.common import TabPane
from graph import graphic


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


def last_balance():
    """ last balance """
    try:
        last_balance = session.query(Operation).filter(Operation.type== "Solde")\
                                            .order_by(Operation.date_op).first()
        return last_balance.value
    except:
        return 0


def consumption():
    pass
    


def graph_for_type(title, type):
    x = [(op.date_op.strftime(u'%d-%m %Hh:%Mmn'))
            for op in session.query(Operation).filter(Operation.type==type)\
                                            .order_by(Operation.date_op).all()]
    y = [(op.value)
                for op in session.query(Operation).filter(Operation.type==type)\
                                        .order_by(Operation.date_op).all()]
    #~ graphic(title, y, '%s (s)' % type, x, 'time (s)')
