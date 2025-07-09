def pregunta_07():
    asociaciones = {}

    with open("files/input/data.csv") as file:
        for line in file:
            columnas = line.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1])

            if valor not in asociaciones:
                asociaciones[valor] = [letra]
            else:
                asociaciones[valor].append(letra)

    return sorted(asociaciones.items())
