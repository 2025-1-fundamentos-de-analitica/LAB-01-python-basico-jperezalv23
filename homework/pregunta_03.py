"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    sumas = {}

    with open("files/input/data.csv") as file:
        for line in file:
            partes = line.strip().split("\t")
            letra = partes[0]
            valor = int(partes[1])
            sumas[letra] = sumas.get(letra, 0) + valor

    return sorted(sumas.items())

