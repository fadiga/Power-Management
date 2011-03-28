#!urs/bin/env
#encoding = utf-8
#maintainer : Fad

from database import *
from datetime import datetime


date_ = datetime(2011, 02, 03)


op = Operation(date_,'jr',1200)

try:
    session.add(op)
    session.commit()
    print "YES"
except:
    session.rollback()
    print "oh no"
