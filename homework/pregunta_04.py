"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    conteo_meses = {}

    with open("files/input/data.csv") as file:
        for line in file:
            columnas = line.strip().split("\t")
            fecha = columnas[2]
            mes = fecha.split("-")[1]
            conteo_meses[mes] = conteo_meses.get(mes, 0) + 1

    return sorted(conteo_meses.items())

