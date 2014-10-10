#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from pyPdf import PdfFileWriter, PdfFileReader



# Variables ===================================================================



# Functions & objects =========================================================
def crop(pdf, left, right, top, bottom):
    out = PdfFileWriter()

    # crop pages
    for page in pdf.pages:
        page.mediaBox.upperRight = (
            page.mediaBox.getUpperRight_x() - right,
            page.mediaBox.getUpperRight_y() - top
        )
        page.mediaBox.lowerLeft = (
            page.mediaBox.getLowerLeft_x() + left,
            page.mediaBox.getLowerLeft_y() + bottom
        )
        out.addPage(page)

    return out


# Main program ================================================================
if __name__ == '__main__':
    pdf = PdfFileReader(
        open("lpm.pdf", 'rb')
    )
    out_pdf = crop(pdf, 50, 50, 50, 50)

    out_file = file("lpm_out.pdf", 'wb')
    out_pdf.write(out_file)
    out_file.close()
