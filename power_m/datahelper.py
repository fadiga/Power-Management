#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from PyQt4 import QtGui

from database import Operation
from ui.common import TabPane


def tabbox(box1, Box2):
    """ adds a box with tab """
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
        last_balance = Operation.select().order_by(("date_op", "desc")).get()
        return last_balance.balance

    except AttributeError:
        raise
        pass


def last_operation(type_op=""):
    """ last operation """
    if type_op != "":
        try:
            return Operation.select().filter(Operation.type == type_op)\
                                               .order_by(("date_op", "desc")).get()

        except:
            raise
            return 0
    else:
        try:
            return Operation.select().\
                             order_by(("date_op", "desc")).get().date_op
        except:
            raise
            pass


def duration():
    """ duration """
    try:
        last_cut = last_operation("cut")
        last_recovery = last_operation("recovery")
        duration = last_recovery.date_op - last_cut.date_op
        return duration, last_recovery.date_op
    except AttributeError:
        pass


def consumption():
    """ Calculation of consumption per day. """
    list_consump = []
    data_balance = [(op.balance, op.date_op, op.type_) for op in Operation.select().order_by(("date_op"))]

    for i in range(len(data_balance) -1):
        if data_balance[i + 1][2] == "balance":
            list_consump.append((data_balance[i][1], abs(int(data_balance[i][0])
                                 - int(data_balance[i + 1][0]))))
    return list_consump


def average_consumption():
    list_consos = []
    for c in consumption():
        list_consos.append(c[1])
    if list_consos != []:
        moy = sum(list_consos) / len(list_consos)
    else:
        moy = 0
    return moy


def estimated_duration():
    balance = int(last_balance())
    avg_conso = int(average_consumption())
    if balance and avg_conso != 0:
        num_days = balance / avg_conso
        return num_days


def max_consumption():
    """ max consumption """
    try:
        lists = consumption()
        l = []
        for c in lists:
            l.append(c[1])
        if len(consumption()) > 1:
            cons = max(l)
            i = l.index(cons)
            return cons, lists[i][0]
        else:
            pass
    except ValueError:
        pass


def balance_graph():
    balance_x = [(op.date_op.strftime(_(u"%d/%b")).decode('utf-8'))
                 for op in Operation.select().filter(type_="balance").order_by(("date_op"))]
    balance_y = [(op.balance) for op in Operation.select()\
                                                 .order_by(("date_op"))\
                                                 .filter(type_="balance")]
    return balance_x, balance_y


def consumption_graph():
    consumption_x = [(cons[0].strftime(_(u"%d/%b")).decode('utf-8'))
                     for cons in consumption()]
    consumption_y = [(cons[1]) for cons in consumption()]
    return consumption_x, consumption_y
