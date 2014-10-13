#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from pyPdf import PdfFileWriter, PdfFileReader



# Variables ===================================================================



# Functions & objects =========================================================
def crop_page(page, left, right, top, bottom):
    page.mediaBox.upperRight = (
        page.mediaBox.getUpperRight_x() - right,
        page.mediaBox.getUpperRight_y() - top
    )
    page.mediaBox.lowerLeft = (
        page.mediaBox.getLowerLeft_x() + left,
        page.mediaBox.getLowerLeft_y() + bottom
    )

    return page


def crop_all(pdf, left, right, top, bottom, remove=[]):
    out = PdfFileWriter()

    # crop pages
    for cnt, page in enumerate(pdf.pages):
        if cnt in remove:
            continue

        out.addPage(
            crop_page(page, left, right, top, bottom)
        )

    return out


def crop_differently(pdf, even_vector, odd_vector, remove=[]):
    out = PdfFileWriter()

    # crop pages
    for cnt, page in enumerate(pdf.pages):
        if cnt in remove:
            continue

        crop_vector = even_vector if cnt % 2 == 0 else odd_vector
        out.addPage(
            crop_page(page, *crop_vector)
        )

    return out


def remove_pages(pdf, remove=[]):
    out = PdfFileWriter()

    # crop pages
    for cnt, page in enumerate(pdf.pages):
        if cnt in remove:
            continue

        out.addPage(page)

    return out


def read_pdf(filename):
    return PdfFileReader(
        open(filename, 'rb')
    )


def save_pdf(filename, content):
    out_file = file(filename, 'wb')
    content.write(out_file)
    out_file.close()
