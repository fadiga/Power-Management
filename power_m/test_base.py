#!urs/bin/env
#encoding = utf-8
#maintainer : Fad

from datetime import datetime

from database import *


date_ = datetime(2011, 02, 03, 10, 30)

op = Operation(date_, 'Solde', 12000)

try:
    session.add(op)
    session.commit()
    print "YES"
except:
    session.rollback()
    print "oh no"
