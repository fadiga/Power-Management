#!/usr/bin/env python
# encoding=utf-8
# maintainer: alou


from gettext import gettext as _
from sqlalchemy import func, desc

from database import Operation, session
from doclib import Document, Text, Table
from doclib.pdf import PDFGenerator
from utils import get_temp_filename, formatted_number
from datahelper import consumption


def build_balance_report(filename=None, format='pdf'):
    ''' PDF: List of balances '''
    if not filename:
        filename = get_temp_filename('pdf')

    doc = Document(title=_(u"List of balances"))

    table = Table(4)
    table.add_header_row([
            Text(_(u"Date")),
            Text(_(u"Type")),
            Text(_(u"Value")),
            Text(_(u"Balance"))])

    # column widths
    table.set_column_width(20, 0)
    table.set_column_width(10, 2)
    table.set_column_width(15, 3)

    # column alignments
    table.set_alignment(Table.ALIGN_LEFT, column=0)
    table.set_alignment(Table.ALIGN_LEFT, column=1)
    table.set_alignment(Table.ALIGN_RIGHT, column=2)
    table.set_alignment(Table.ALIGN_RIGHT, column=3)

    operations = [(op.date_op, op.type, op.value, op.balance ) \
                    for op in session.query(Operation) \
                    .filter(Operation.type=='balance')
                    .order_by(desc(Operation.date_op)).all()]

    for operation in operations:
        table.add_row([
            Text(unicode(operation[0])),
            Text(unicode(operation[1])),
            Text(formatted_number(operation[2])),
            Text(formatted_number(operation[3]))])

    doc.add_element(table)

    gen = PDFGenerator(doc, filename)
    gen.render_document()

    return gen.get_filename()


def build_consumption_report(filename=None, format='pdf'):
    ''' PDF: List of consumptions '''
    if not filename:
        filename = get_temp_filename('pdf')

    doc = Document(title=_(u"List of consumptions"))

    table = Table(2)
    table.add_header_row([
            Text(_(u"Date")),
            Text(_(u"Consumption"))])

    # column alignments
    table.set_alignment(Table.ALIGN_LEFT, column=0)
    table.set_alignment(Table.ALIGN_LEFT, column=1)

    operations = [(op[0], op[1]) for op in consumption()]

    for operation in operations:
        table.add_row([
            Text(unicode(operation[0])),
            Text(unicode(operation[1]))])

    doc.add_element(table)

    gen = PDFGenerator(doc, filename)
    gen.render_document()

    return gen.get_filename()
