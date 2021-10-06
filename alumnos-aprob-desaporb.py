"""
[ Tarea ]
Ingrese la cantidad de alumnos de la cátedra, luego por cada uno indique si entregaron el TP1. 
    - Indicar qué porcentaje de alumnos entregó el TP
    - Indicar cuántos alumnos no lo entregaron
    
    PARECE BASTANTE PERO SON COMENTARIOS Y PRINTS DE MAS PARA DARLE COLOR
"""

# Input catidad de alumnos
alumnos = int(input('Ingrese la cantidad de alumnos de la catedra: '))

# Crear variable de quienes entregaron
entregaron = 0

print('[ Indique alumno x alumno si entrego o no con: s/n o si/no         ]')
print('[ Ejemplo: Entrego? s                                              ]')
print('[ Si es diferente a esos valores se va a marcar como no entregado! ]\n')

# Tomar x de inputs
for i in range(0, alumnos):
    # Nuevo input
    entrega = input('Indique si el alumno entrego (s/n): ')
    print(f'Se marco al almuno {i+ 1}/{alumnos} como {entrega}')

    # Si el input es s suma +1 a los entregados
    if entrega == 's' or entrega == 'si':
        entregaron += 1

print('Calculando resultados...')

# Ver si es 0 para que no tire error
porcEntregaron = 0
if entregaron > 0:
    # Sacar porcentaje
    porcEntregaron = (entregaron * 100) / alumnos

print('resultados calculados!')

# Resultados
print(f"""
    Total Alumnos Catedra: {alumnos}
    -Total Entregaron: {entregaron}
    -Porcentaje Entregado: {porcEntregaron}%
    -Total No entregado: {alumnos - entregaron}
""")
