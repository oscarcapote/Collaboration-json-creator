# Collaboration-json-creator

Programa que a partir de una llista de investigador-article genera una xarxa de col·laboració en format JSON
## Dependències:
Python3
NetworkX: [link](https://networkx.github.io/)
Llibreria de detecció de comiunitats amb mètode de Louvain: [link](https://bitbucket.org/taynaud/python-louvain)

## Arxiu de input:
L'arxiu ha de estar en codificació utf8 emprant com a separador de columnes §.
La primera columna ha de ser el nom de l'investigador i a la segona l'article publicat.
Per exemple:
John Smith§Estudis de vibracions

L'arxiu s'ha de posar a la carpeta `input_file`.

## Execució:
Per executar el programa `json_maker.py` has de executar la comanda:
'''
python3 json_maker.py nom_arxiu
'''
On `nom_arxiu` és el nom de l'arxiu que està a la capeta `input_file`. Si no es posa l'argument, el programa automàticament cercarà un arxiu de nom `networksociocomplex.txt` per defecte.

Una vegada acabats els càlculs, el programa crea un arxiu a la carpeta `output_json` amb el mateix nom que l'input però canviant la extensió a `.json`
