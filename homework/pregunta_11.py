import pandas as pd

def pregunta_11():
    """
    Construye una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c4` del archivo `tbl1.tsv`.

    Retorna:
    Un DataFrame con `c0` y `c4`, donde `c4` contiene los valores únicos
    de `c4` separados por ',' y ordenados alfabéticamente.

    Ejemplo de salida:
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """

    # Cargar el archivo tbl1.tsv
    tbl1 = pd.read_csv('files/input/tbl1.tsv', sep='\t')

    # Agrupar por c0 y concatenar valores únicos de c4 en orden alfabético
    grouped = tbl1.groupby('c0')['c4'].apply(lambda x: ','.join(sorted(set(x))))

    # Convertir la serie en un DataFrame y resetear el índice
    result = grouped.reset_index()

    return result
