pdf_cropper.py
==============

Ořezávač PDF souborů. Jedná se o shellscript pro unixový operační systém, který
umožňuje jednak upravovat rozměry PDF souborů "odříznutím" částí stránek,
dále pak i odstraňovat vybrané stránky.

Překlad nápovědy::

  použití: pdf_cropper.py [-h] [-c X X X X] [-e X X X X] [-r STR [STR ...]]
                          [-o VYSTUP]
                          soubor

  Ořezávač PDF souborů. Tento program může byt použit k ořezu a odstraňování
  stránek z PDF souborů.

  positional arguments:
    soubor                Název vstupního souboru.

  optional arguments:
    -h, --help            Zobraz tuto nápovědu.
    -c X X X X, --crop X X X X
                          Ořezový vektor pro všechny, či sudé stránky. Vektor
                          je očekáván ve formátu LEVÁ PRAVÁ NAHOŘE DOLE.
                          Například -c 50 50 10 10.
    -e X X X X, --crop-odd X X X X
                          Ořezový vektor pro liché stránky. Vektor je očekáván
                          ve formátu LEVÁ PRAVÁ NAHOŘE DOLE. Například -c 50
                          50 10 10.
    -r STR [STR ...], --remove STR [STR ...]
                          Odstraň následující strany. Čísla stran začínají od
                          nuly.
    -o VYSTUP, --output VYSTUP
                          Ulož upravený soubor do následující cesty. Pokud
                          není nastaveno, používá se přípona '_cropped.pdf'.

Ukázka použití::

  ./pdf_cropper.py -c 10 10 5 5 -r 0 -- ukazka01b.pdf

Uvedený příklad ořízne soubor :download:`ukazka01b.pdf </_static/ukazka01b.pdf>`
deset milimetrů z leva a z prava a pět milimetrů zezhora a zezdola. Parametr
``-r`` či ``--remove`` odstraní stránku na indexu ``0``.

Výsledek je možné vidět v souboru in :download:`ukazka01b_cropped.pdf
</_static/ukazka01b_cropped.pdf>`.
