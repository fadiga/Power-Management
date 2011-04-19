#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from PyQt4 import QtGui

from sqlalchemy import desc, asc

from database import Operation, session
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
        pass


def last_operation(type_op=''):
    """ last cou """
    if type_op != '':
        try:
            last_operation = session.query(Operation).\
                        filter(Operation.type == type_op).\
                        order_by(desc(Operation.date_op)).first()
            return last_operation
        except:
            return 0
    else:
        try:
            last_operation = session.query(Operation).\
                        order_by(desc(Operation.date_op)).first()
            return last_operation.date_op
        except:
            pass


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
                            order_by(asc(Operation.date_op))]

    for i in range(len(data_balance) -1):
        if data_balance[i][2] == "balance" and data_balance[i+1][2] == "balance":
            list_consump.append((data_balance[i][1],\
                        abs(data_balance[i][0] - data_balance[i + 1][0])))


    return list_consump

def average_consumption():
    list_consos = []
    for c in consumption():
        list_consos.append(c[1])
    moy = sum(list_consos)/len(list_consos)
    return moy


def estimated_duration():
    balance = last_balance()
    avg_conso = average_consumption()
    num_days = balance/avg_conso
    return num_days


def max_consumption():
    """ max consumption """
    try:
        if len(consumption()) > 1:
            cons = max(consumption())
            return cons
        else:
            pass
    except ValueError:
        pass


def graph_for_type(type):
    x = []
    y = []
    if type == u"balance":
        x = [(op.date_op.strftime(_(u' %d/%b')))
                        for op in session.query(Operation).\
                            order_by(asc(Operation.date_op))\
                            .filter(Operation.type == 'balance').all()]
        y = [(op.balance) for op in session.query(Operation)\
                            .order_by(asc(Operation.date_op))\
                            .filter(Operation.type == 'balance').all()]
    if type == u"consumption":
        x = [(cons[0].strftime(_(u'%d/%b')))
            for cons in consumption()]
        y = [(cons[1])
            for cons in consumption()]
    graphic(y, type, x)

graph_for_type("")
