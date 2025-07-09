"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    valores = {}

    with open("files/input/data.csv") as file:
        for line in file:
            partes = line.strip().split("\t")
            letra = partes[0]
            numero = int(partes[1])

            if letra not in valores:
                valores[letra] = [numero, numero]  # [max, min]
            else:
                valores[letra][0] = max(valores[letra][0], numero)
                valores[letra][1] = min(valores[letra][1], numero)

    resultado = [(letra, valores[letra][0], valores[letra][1]) for letra in sorted(valores)]
    return resultado

