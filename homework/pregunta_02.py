"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    with open("files/input/data.csv") as file:
        conteo = {}

        for line in file:
            letra = line[0]
            conteo[letra] = conteo.get(letra, 0) + 1

    return sorted(conteo.items())

