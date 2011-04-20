#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer : Fad

from matplotlib.ticker import FuncFormatter
from pylab import *


def graphic(datay, typey, datax):
    ''' is the graph
       param :
            datay = data y (list)
            typey = label y (string)
            datax = data x (list)
    '''

    x = arange(len(datay))
    ax = subplot(312)
    grid(True)
    bar(x, datay)
    xticks(x + 0.1, datax)
    labels = ax.get_xticklabels()
    setp(labels, rotation=30, fontsize=12)

    if typey == u"balance":
        savefig('graph_banlance.png', dpi=50)

    if typey == "consumption":
        savefig('graph_consumption.png', dpi=50)
