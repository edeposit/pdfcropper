#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import sys
import os.path
import argparse

import pdfcropper


# Variables ===================================================================



# Functions & objects =========================================================



# Main program ================================================================
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""PDF cropper. This program can be used to crop and remove
                       pages from PDF files."""
    )
    parser.add_argument(
        "-c",
        "--crop",
        nargs=4,
        metavar="X",
        help="""Crop vector for all or odd pages. Vector is in format LEFT
                RIGHT TOP BOTTOM. -c 50 50 10 10 for example."""
    )
    parser.add_argument(
        "-e",
        "--crop-even",
        nargs=4,
        metavar="X",
        help="""Crop vector for even pages. Vector is in format LEFT RIGHT TOP
                BOTTOM. -c 50 50 10 10 for example."""
    )
    parser.add_argument(
        "-r",
        "--remove",
        nargs="+",
        metavar="PAGE",
        help="Remove following pages. Page numbers starts from zero."
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs=1,
        help="""Save modified file to given destination. Use - for stdout. If
                not set, suffix '_cropped.pdf' is used."""
    )
    parser.add_argument(
        "filename",
        help="Input filename."
    )
    args = parser.parse_args()

    if not os.path.exists(args.filename):
        sys.stderr.write("Can't open '%s'!\n" % args.filename)
        sys.exit(1)

    print args
