"""
    Tarea

    Ingresar cant alumnos de catdra
    x cada uno ver si se entrego tp1
    % de alumnos q entrego
    cuantos no entregaron
"""

alumnos = int(input('Ingrese la cantidad de alumnos de la catedra: '))

entregaron = 0
noEntregaron = 0

print('Indique alumno x alumno si entrego o no con: s/n')
print('Ejemplo: Entrego? s')
for i in range(0, alumnos + 1):
    entrega = input('Indique si el alumno entrego (s/n): ')

    if entrega == 's':
        entregaron += 1
    elif entrega == 'n':
        noEntregaron += 1

print(f"""
    Total Alumnos Catedra: {alumnos}
    -Total Entregaron: {entregaron}
    -Promedio Entregado: {alumnos / entregaron}
    =
    -Total No entregado: {noEntregaron}
    -Promedio No Entregado: {alumnos / noEntregaron}
""")
