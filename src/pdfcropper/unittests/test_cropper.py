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
def aprx_same(a, b, t=0.0001):
    return abs(a - b) < t


# Tests =======================================================================
def test_read_pdf():
    pdf = cropper.read_pdf(DATA_FILE)

    assert isinstance(pdf, pyPdf.PdfFileReader)
    assert len(pdf.pages) >= 2


def test_get_width_height():
    pdf = cropper.read_pdf(DATA_FILE)

    width, height = cropper.get_width_height(pdf.pages[0])

    assert int(width) == 174
    assert int(height) == 236


def test_crop_page():
    pdf = cropper.read_pdf(DATA_FILE)

    cropped = cropper.crop_page(pdf.pages[0], 10, 10, 10, 10)

    # original dimensions are taken here for purpose to test, that the deep
    # copy of page was really created
    original_width, original_height = cropper.get_width_height(pdf.pages[0])
    cropped_width, cropped_height = cropper.get_width_height(cropped)

    assert aprx_same(original_width - cropped_width, 20)
    assert aprx_same(original_height - cropped_height, 20)