import pandas as pd

def pregunta_12():
    """
    Construye una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a` y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Retorna:
    Un DataFrame con `c0` y `c5`, donde `c5` contiene valores de `c5a:c5b`
    concatenados y separados por ','.

    Ejemplo de salida:
         c0                                   c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """

    # Cargar el archivo tbl2.tsv
    tbl2 = pd.read_csv('files/input/tbl2.tsv', sep='\t')

    # Concatenar c5a y c5b con ':'
    tbl2['c5'] = tbl2['c5a'] + ':' + tbl2['c5b'].astype(str)

    # Agrupar por c0 y concatenar los valores de c5 separados por ','
    grouped = tbl2.groupby('c0')['c5'].apply(lambda x: ','.join(sorted(x)))

    # Convertir la serie en un DataFrame y resetear el índice
    result = grouped.reset_index()

    return result
