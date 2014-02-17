#!/usr/bin/env python
# encoding=utf-8
# Autor: Fadiga

from models import  (Operation)



def setup(drop_tables=False):
    """ create tables if not exist """

    did_create = False

    for model in [Operation,]:
        if drop_tables:
            model.drop_table()
        if not model.table_exists():
            model.create_table()
            did_create = True

    if did_create:
        print(u"---- Creation de la BD -----")