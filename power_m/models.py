#!/usr/bin/env python
# encoding=utf-8
# Autor: Fadiga

import peewee

from gettext import gettext as _
from datetime import date, datetime

DATE_FMT = u'%A %d %B %Y'
DB_FILE = "power_mg.db"
dbh = peewee.SqliteDatabase(DB_FILE)


class BaseModel(peewee.Model):

    class Meta:
        database = dbh

    @classmethod
    def all(cls):
        return list(cls.select())


class Operation(BaseModel):
    """ Operations """

    date_op = peewee.DateTimeField(max_length=30, verbose_name=u"Date")
    type_ = peewee.CharField(max_length=30, verbose_name=u"Type")
    value = peewee.CharField(max_length=30, verbose_name=u"Value")
    balance = peewee.CharField(max_length=30, verbose_name=u"balance")

    def __unicode__(self):
        return u"{value}".format(value=self.value)

    def display_name(self):
        return self.value.title()
