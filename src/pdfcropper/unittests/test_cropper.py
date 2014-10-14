#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import os
import os.path

import pyPdf

import pdfcropper.cropper as cropper


# Variables ===================================================================
DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "ukazka01b.pdf")


# Functions & objects =========================================================



# Tests =======================================================================
def test_read_pdf():
    pdf = cropper.read_pdf(DATA_FILE)

    assert isinstance(pdf, pyPdf.PdfFileReader)