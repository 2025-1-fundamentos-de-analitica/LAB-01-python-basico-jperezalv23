def pregunta_08():
    asociaciones = {}

    with open("files/input/data.csv") as file:
        for line in file:
            columnas = line.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1])

            if valor not in asociaciones:
                asociaciones[valor] = set()
            asociaciones[valor].add(letra)

    # Convertir el set en lista ordenada
    resultado = [(valor, sorted(list(letras))) for valor, letras in sorted(asociaciones.items())]
    return resultado
