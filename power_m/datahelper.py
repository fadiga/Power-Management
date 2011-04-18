#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from PyQt4 import QtGui
from datetime import date, datetime
from sqlalchemy import desc

from database import *
from ui.common import TabPane
from graph import graphic


def tabbox(box1, Box2):
    ''' adds a box with tab '''
    tab_widget = QtGui.QTabWidget()
    for heading in [_("Graphe"), _("Table")]:
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
        return last_balance.balance

    except AttributeError:
        return None


def last_operation(type_op):
    """ last cou """
    try:
        last_operation = session.query(Operation).\
                    filter(Operation.type == type_op).\
                    order_by(desc(Operation.date_op)).first()
        return last_operation

    except:
        return 0


def duration():
    """ duration """
    try:
        last_cut = last_operation('cut')
        last_recovery = last_operation('recovery')

        duration = last_recovery.date_op - last_cut.date_op
        return duration, last_recovery.date_op
    except AttributeError:
        pass


def consumption():
    """ Calculation of consumption per day."""
    list_consump = []
    data_balance = [(op.balance,\
                    op.date_op,\
                    op.type)\
                            for op in session.query(Operation).\
                            order_by(desc(Operation.date_op))]

    for i in range(len(data_balance) - 1):
        if data_balance[i][2] == "balance":
            list_consump.append((data_balance[i][1],\
                        abs(data_balance[i + 1][0] - data_balance[i][0])))
    return list_consump


def max_consumption():
    """ max consumption """
    try:
        cons = max(consumption())
        return cons
    except ValueError:
        pass


def graph_for_type(title, type):
    x = []
    y = []

    if type == u"consumption":
        x = [(cons[0].strftime(_(u'%d/%b')))
            for cons in consumption()][:5]
        y = [(cons[1])
            for cons in consumption()][:5]

    elif type == u"balance":
        x = [(op.date_op.strftime(_(u' %d/%b')))
        for op in session.query(Operation).\
                            order_by(desc(Operation.date_op)).all()][:5]
        y = [(op.value) for op in session.query(Operation)\
                            .order_by(desc(Operation.date_op))\
                            .filter(Operation.type == 'balance').all()][:5]
    graphic(title, y, type, x, u'time (s)')

graph_for_type(u"", u"")
