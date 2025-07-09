def pregunta_06():
    resultados = {}

    with open("files/input/data.csv") as file:
        for line in file:
            columnas = line.strip().split("\t")
            pares = columnas[4].split(",")

            for par in pares:
                clave, valor = par.split(":")
                valor = int(valor)

                if clave not in resultados:
                    resultados[clave] = [valor, valor]
                else:
                    resultados[clave][0] = min(resultados[clave][0], valor)
                    resultados[clave][1] = max(resultados[clave][1], valor)

    return sorted((clave, minimo, maximo) for clave, (minimo, maximo) in resultados.items())
