#!/usr/bin/env python
# encoding = utf-8
# maintainer : Fad

from matplotlib.ticker import FuncFormatter
from pylab import *

from database import *

data = [(op.valeur)
            for op in session.query(Operation).all()]
x = arange(len(data))
dates = [(op.date_op)
            for op in session.query(Operation).all()]


def millions(x, pos):
    'The two args are the value and tick position'
    return '%s' % (x)

formatter = FuncFormatter(millions)

ax = subplot(211)
ax.yaxis.set_major_formatter(formatter)
title('Representation graphique')
xlabel('time (s)')
ylabel('Solde (s)')
grid(True)
bar(x, data)
xticks(x + 0.5, dates)
show()
