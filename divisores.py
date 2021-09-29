    """
    leer un numero e indicar sus divisores
    """
    num = int(input('Ingrese el numero para ver los divisores: '))
    contador = 0
    numeros = ''
    for divisor in range(1, num + 1):
        if (num % divisor) == 0:
            numeros += str(divisor) + ' | '
            contador += 1
    print('El numero', num, ' tiene (', numeros, ') como divisores')
