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
        last_balance = session.query(Operation).\
                                    order_by(desc(Operation.date_op)).first()
        return last_balance.value
    except AttributeError:
        return None


def consumption():
    """ Calculation of consumption per day."""
    list_consump = []
    data_balance = [(op.balance,\
                    op.date_op.strftime(u'%d-%m-%Y %Hh:%Mmn'))\
                            for op in session.query(Operation).\
                            filter(Operation.type == "Solde").\
                            filter(Operation.type == "Ajout").\
                            order_by(Operation.date_op)]

    for i in range(len(data_balance) - 1):
        list_consump.append((data_balance[i][1],\
                    abs(data_balance[i + 1][0] - data_balance[i][0])))
    return list_consump


def graph_for_type(title, type):
    x = [(op.date_op.strftime(u'%d-%m-%Y %Hh:%Mmn'))
        for op in session.query(Operation).filter(Operation.type == type).\
                                    order_by(Operation.date_op).all()]
    y = [(op.value) for op in session.query(Operation).\
                            filter(Operation.type == type).\
                            order_by(Operation.date_op).all()]
    #~ graphic(title, y, '%s (s)' % type, x, 'time (s)')
