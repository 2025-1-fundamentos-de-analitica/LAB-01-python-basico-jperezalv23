def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    resultado = []
    with open("files/input/data.csv") as f:
        for linea in f:
            partes = linea.strip().split('\t')
            letra = partes[0]
            col4 = partes[3].split(',') if partes[3] else []
            col5 = partes[4].split(',') if partes[4] else []
            resultado.append((letra, len(col4), len(col5)))
    return resultado
