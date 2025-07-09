def pregunta_09():
    conteo = {}

    with open("files/input/data.csv") as file:
        for line in file:
            columnas = line.strip().split("\t")
            pares = columnas[4].split(",")

            for par in pares:
                clave = par.split(":")[0]
                conteo[clave] = conteo.get(clave, 0) + 1

    return dict(sorted(conteo.items()))
