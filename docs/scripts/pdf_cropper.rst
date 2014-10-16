pdf_cropper.py
==============

Test script used to show output of all downloaded data.

Help::

  usage: pdf_cropper.py [-h] [-c X X X X] [-e X X X X] [-r PAGE [PAGE ...]]
                        [-o OUTPUT]
                        filename

  PDF cropper. This program can be used to crop and remove pages from PDF files.

  positional arguments:
    filename              Input filename.

  optional arguments:
    -h, --help            show this help message and exit
    -c X X X X, --crop X X X X
                          Crop vector for all or even pages. Vector is in format
                          LEFT RIGHT TOP BOTTOM. -c 50 50 10 10 for example.
    -e X X X X, --crop-odd X X X X
                          Crop vector for odd pages. Vector is in format LEFT
                          RIGHT TOP BOTTOM. -c 50 50 10 10 for example.
    -r PAGE [PAGE ...], --remove PAGE [PAGE ...]
                          Remove following pages. Page numbers starts from zero.
    -o OUTPUT, --output OUTPUT
                          Save modified file to given destination. If not set,
                          suffix '_cropped.pdf' is used.

Example of the use::

  ./pdf_cropper.py -c 10 10 5 5 -r 0 -- ukazka01b.pdf

Which will crop the file :download:`ukazka01b.pdf </_static/ukazka01b.pdf>` ten
millimeters from left and right and five millimeters from up and down. ``-r`` or
``--remove`` parameter will also remove page at index ``0``. Result can be seen
in :download:`ukazka01b_cropped.pdf </_static/ukazka01b_cropped.pdf>`.