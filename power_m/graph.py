#!/usr/bin/env python
# encoding = utf-8
# maintainer : Fad

from matplotlib.ticker import FuncFormatter
from pylab import *

from database import *


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
    ax = subplot(211)
    ax.yaxis.set_major_formatter(formatter)
    title(titleg)
    xlabel(labelx)
    ylabel(labely)
    grid(True)
    bar(x, datay)
    xticks(x + 0.5,  datax )
    labels = ax.get_xticklabels()
    setp(labels, rotation=30, fontsize=10)
    show()


def ff(x, pos):
    'The two args are the value and tick position'
    return '%s' % (x)


x = [(op.date_op.strftime(u'%d-%m %Hh:%Mmn'))
            for op in session.query(Operation).all()]        
y = [(op.valeur)
            for op in session.query(Operation).all()]
                
graphic('Representation graphique du solde par jour', y, 'Solde (s)', x, 'time (s)')
