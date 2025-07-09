def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    resultado = {}
    with open("files/input/data.csv") as f:
        for linea in f:
            partes = linea.strip().split('\t')
            clave = partes[0]
            valores_col5 = partes[4].split(',')
            suma = sum(int(item.split(':')[1]) for item in valores_col5)
            if clave in resultado:
                resultado[clave] += suma
            else:
                resultado[clave] = suma
    return resultado
