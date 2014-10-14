#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from pyPdf import PdfFileWriter, PdfFileReader


# Functions & objects =========================================================
def crop_page(page, left, right, top, bottom):
    """
    Crop `page` to size given by `left`, `right`, `top` and `bottom`.

    Args:
        page (obj): :mod:`pyPdf` PdfFileReader's page object.
        left (int): Cut X millimeters from left.
        right (int): Cut X millimeters from right.
        top (int): Cut X millimeters from top.
        bottom (int): Cut X millimeters from bottom.

    Warning:
        This functions modieies the `page` reference!

    Returns:
        obj: Modified page object.
    """
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
    """
    Crop all pages in `pdf`. Remove pages specified by `remove`.

    Args:
        pdf (obj): :mod:`pyPdf` :class:`PdfFileReader` object.
        left (int): Cut X millimeters from left.
        right (int): Cut X millimeters from right.
        top (int): Cut X millimeters from top.
        bottom (int): Cut X millimeters from bottom.
        remove (list/tuple, default []): List of integers. As the function
               iterates thru the pages in `pdf`, indexes of the pages which
               matchs those in `remove` will be skipped.

    Returns:
        obj: :class:`PdfFileWriter` instance.
    """
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
    with file(filename, 'wb') as f:
        content.write(f)
