PDF cropper
===========

This project is aimed to provide simple and easy to use script for cropping
PDF files as part of the E-deposit project.

Česká verze
-----------

- :doc:`/index_cz`

Script
------

From user's point of view, following script is his interface with pdfcropper:

.. toctree::
    :maxdepth: 1

    /scripts/pdf_cropper

API
---

From programmer's point of view, there are few collections of functions, which
he (or she) may use:

.. toctree::
    :maxdepth: 1

    /api/pdfcropper
    /api/pdfcropper.cropper

Source code
-----------
This project is released as opensource (GPL) and source codes can be found at
GitHub:

- https://github.com/edeposit/pdfcropper

Installation
------------
Module is hosted at `PYPI <https://pypi.python.org/pypi/pdfcropper>`_,
and can be easily installed using
`PIP <http://en.wikipedia.org/wiki/Pip_%28package_manager%29>`_:

::

    sudo pip install pdfcropper

Testing
-------
Almost every feature of the project is tested in unit/integration tests. You
can run this tests using provided ``run_tests.sh`` script, which can be found
in the root of the project.

Requirements
++++++++++++
This script expects that pytest_ is installed. In case you don't have it yet,
it can be easily installed using following command::

    pip install --user pytest

or for all users::

    sudo pip install pytest

.. _pytest: http://pytest.org/