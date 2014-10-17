PDF ořezávač
============

Cílem tohoto projektu je poskytnout script pro ořezávání PDF souborů, jako
součást projektu E-deposit.

English version
---------------

- :doc:`/index`

Script
------

Z uživatelského hlediska je dostupný následující script:

.. toctree::
    :maxdepth: 1

    /scripts/pdf_cropper_cz

API
---

Z programátorského hlediska je dostupno několik funkcí, které je možné použít
k úpravám PDF souborů.

.. toctree::
    :maxdepth: 1

    /api/pdfcropper
    /api/pdfcropper.cropper

Zdrojový kód
------------
Ořezávač je dostupný pod opensource licencí GPL. Kompletní zrojový kód je možné
najít na serveru GitHub:

- https://github.com/edeposit/pdfcropper

Instalace
---------
Celý softwarový balíček je hostovaný na `PYPI
<https://pypi.python.org/pypi/pdfcropper>`_, a může být jednoduše nainstalován
pomocí programu `PIP <http://en.wikipedia.org/wiki/Pip_%28package_manager%29>`_:

::

    sudo pip install pdfcropper

Testování
---------
Téměř všechny funkce dostupné v softwarovém balíčku jsou tostovány pomocí
unittestů. Tyto je možné spustit použitím scriptu ``run_tests.sh``, který se
nachází v kořenovém adresáři projektu.

Požadavky
+++++++++
Testovací script vyžaduje pytest_. Pokud ho nemáte nainstalovaný, můžete ho
jednoduše doinstalovat použitím následujícího příkazu:

    sudo pip install pytest

.. _pytest: http://pytest.org/