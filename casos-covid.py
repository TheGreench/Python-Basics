"""
    lista de casoss + covid x pais
    Indicar prom mundial
    cantidad de casos
    cantidad de casos < pais
    cantidad de casos > pais
    """

    print('Para terminar ingrese el -1')
    casos = int(input('Cantidad de casos: '))
    paises = 0
    totalCasos = 0
    menorPais = casos
    mayorPais = casos

    while casos != -1:
        paises += 1
        totalCasos += casos

        if casos > mayorPais:
            mayorPais = casos
        elif casos < menorPais:
            menorPais = casos

        casos = int(input('Cantidad de casos: '))

    if paises > 0:
        promedio = totalCasos / paises

        print(f"""
        El promedio mundial es: {promedio}
        El total de casos es: {totalCasos}
        El menor numero de casos es: {menorPais}
        El menor numero de casos es: {mayorPais}
        """)
