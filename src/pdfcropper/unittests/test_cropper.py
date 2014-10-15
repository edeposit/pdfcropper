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
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
DATA_FILE = os.path.join(DATA_DIR, "ukazka01b.pdf")
TMP_FILE = os.path.join(DATA_DIR, "tmp_file.pdf")


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
    original_width, original_height = cropper.get_width_height(pdf.pages[0])

    cropped = cropper.crop_page(pdf.pages[0], 10, 10, 10, 10)
    cropped_width, cropped_height = cropper.get_width_height(cropped)

    assert aprx_same(original_width - cropped_width, 20)
    assert aprx_same(original_height - cropped_height, 20)


def test_crop_all():
    pdf = cropper.read_pdf(DATA_FILE)
    dimensions_list = map(
        lambda x: cropper.get_width_height(x),
        pdf.pages
    )

    new_pdf = cropper.crop_all(pdf, 10, 10, 10, 10)
    cropper.save_pdf(TMP_FILE, new_pdf)

    new_pdf = cropper.read_pdf(TMP_FILE)

    # check that all pages were cropped
    for pagenum, page in enumerate(new_pdf.pages):
        original_width, original_height = dimensions_list[pagenum]
        cropped_width, cropped_height = cropper.get_width_height(page)

        assert aprx_same(original_width - cropped_width, 20)
        assert aprx_same(original_height - cropped_height, 20)


def test_crop_all_remove():
    pdf = cropper.read_pdf(DATA_FILE)

    new_pdf = cropper.crop_all(pdf, 10, 10, 10, 10, remove=[0])
    cropper.save_pdf(TMP_FILE, new_pdf)

    new_pdf = cropper.read_pdf(TMP_FILE)

    assert len(pdf.pages) == 2
    assert len(new_pdf.pages) == 1


def test_crop_differently():
    pass


def test_remove_pages():
    pass


def test_save_pdf():
    pass


def teardown_module():
    if os.path.exists(TMP_FILE):
        os.unlink(TMP_FILE)
