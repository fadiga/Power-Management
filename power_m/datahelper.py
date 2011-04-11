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
                    filter(Operation.type=="Solde")\
                    .order_by(Operation.date_op).first()
        return last_balance.value
    except:
        return 0
        
        
def last_operation(type_):
    """ last cou """
    try:
        last_operation = session.query(Operation).\
                    filter(Operation.type==type_)\
                    .order_by(desc(Operation.date_op)).first()
        return last_operation

    except:
        return 0

def duration():
    """ duration """
    
    last_coupure = last_operation('Coupure')
    last_reprise = last_operation('Reprise')

    duration = last_reprise.date_op - last_coupure.date_op
    return duration, last_reprise.date_op


def consumption():
    """ Calculation of consumption per day."""
    dic = []
    data_balance = [(op.balance,\
                    op.date_op.strftime(u'%d-%m-%Y %Hh:%Mmn'))\
                            for op in session.query(Operation).filter(Operation.type=="Solde").\
                            order_by(Operation.date_op)]

    for i in range(len(data_balance) - 1):
        dic.append((data_balance[i][1],\
                    abs(data_balance[i+1][0] - data_balance[i][0])))
    return dic


def max_consumption():
    """ max consumption """
    cons = max(consumption())
    return cons


def graph_for_type(title, type):
    x = [(op.date_op.strftime(u'%d-%m-%Y %Hh:%Mmn'))
        for op in session.query(Operation).filter(Operation.type==type)\
                                    .order_by(Operation.date_op).all()]
    y = [(op.value)
        for op in session.query(Operation).filter(Operation.type==type)\
                                    .order_by(Operation.date_op).all()]
    #~ graphic(title, y, '%s (s)' % type, x, 'time (s)')
