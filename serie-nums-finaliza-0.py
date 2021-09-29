"""Ejercicio de Tarea:
- Ingresar una serie de numeros finalizada en 0
- Indicar si el ingreso se hizo ordenadamente o desordenamente
+ Ejemplos:
1 4 65 78 198 0 = Serie ordenada
6 45 9 22 0     = Serie desordenada
"""
# Primer input
num = int(input('Ingrese un numero: '))
valor = 0
ordenado = True

# sigue con inputs hasta que el numero sea 0
while num != 0:
    # guarda el numero anterior
    valor = num
    # guarda el nuevo numero
    num = int(input('Ingrese un numero: '))

    # compara si el numero anterior es > al nuevo
    if valor > num != 0:
        # si es mayor ya la lista esta desordenada
        ordenado = False

if ordenado:
    print('Serie ingresada esta ordenada!')
else:
    print('Serie ingresada esta desordenada!')
