#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer : Fad

from matplotlib.ticker import FuncFormatter
from pylab import *


def graphic(datay, typey, datax):
    ''' is the graph
       param :
            datay = data y (list)
            labely = label y (string)
            datax = data x (list)
            labelx = label x (string)
    '''

    x = arange(len(datay))
    formatter = FuncFormatter(ff)
    ax = subplot(312)
    ax.yaxis.set_major_formatter(formatter)
    #~ xlabel(labelx)
    #~ ylabel(labely)
    grid(True)
    bar(x, datay)
    xticks(x + 0.1,  datax)
    labels = ax.get_xticklabels()
    setp(labels, rotation=30, fontsize=12)

    if typey == u"balance":
        savefig('graph_banlance.png', dpi=57)

    elif typey == "consumption":
        savefig('graph_consumption.png', dpi=57)


def ff(x, pos):
    'The two args are the value and tick position'
    return u'%s' % (x)
