def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    resultado = {}
    with open("files/input/data.csv") as file:
        for linea in file:
            partes = linea.strip().split('\t')
            valor = int(partes[1])
            letras = partes[3].split(',')
            for letra in letras:
                if letra in resultado:
                    resultado[letra] += valor
                else:
                    resultado[letra] = valor
    return dict(sorted(resultado.items()))
