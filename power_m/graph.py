#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer : Fad

from matplotlib.ticker import FuncFormatter
from pylab import *

def graphic(titleg, datay, labely, datax, labelx):
    ''' is the graph
       param :
            titleg = the title (string)
            datay = data y (liste)
            labely = label y (string)
            datax = data x (liste)
            labelx = label x (string)
    '''
    x = arange(len(datay))
    formatter = FuncFormatter(ff)
    ax = subplot(312)
    ax.yaxis.set_major_formatter(formatter)
    title(titleg)
    xlabel(labelx)
    ylabel(labely)
    grid(True)
    bar(x, datay)
    xticks(x + 0.1,  datax )
    labels = ax.get_xticklabels()
    setp(labels, rotation=10, fontsize=12)
    savefig('graph.png',dpi=52)


def ff(x, pos):
    'The two args are the value and tick position'
    return '%s' % (x)

