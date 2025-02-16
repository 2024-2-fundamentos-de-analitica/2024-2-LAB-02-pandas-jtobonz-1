"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """

    # Se importa la libreria pandas
    import pandas as pd

    # Se lee el archivo tbl1.tsv
    tbl1 = pd.read_csv('files/input/tbl1.tsv', sep='\t')

    # Se extraen los valores unicos de la columna c4
    return sorted(tbl1['c4'].str.upper().unique())