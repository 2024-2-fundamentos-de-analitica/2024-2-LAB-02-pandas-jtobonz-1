import pandas as pd

def pregunta_10():
    """
    Construye una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Retorna:
    Un DataFrame con `_c1` como índice y `c2` con los valores ordenados y separados por ':'.

    Ejemplo de salida:
                                 c2
    _c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """

    # Cargar el archivo tbl0.tsv
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    # Agrupar por 'c1' y concatenar los valores de 'c2' ordenados
    grouped = tbl0.groupby('c1')['c2'].apply(lambda x: ':'.join(sorted(x.astype(str))))

    # Convertir en DataFrame y renombrar el índice a '_c1'
    result = grouped.to_frame().rename_axis('_c1')

    return result
