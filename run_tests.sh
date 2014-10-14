#! /usr/bin/env bash

PYTHONPATH="$PYTHONPATH:src/"
TEST_PATH="src/pdfcropper/unittests/"

py.test "$TEST_PATH"