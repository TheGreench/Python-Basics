"""
Escribir un programa que simule el proceso de control de peso y cantidad de personas que puede transportar un ascensor.
Vamos a suponer que nuestro ascensor puede soportar un máximo de 400 kg y hasta 6 personas.
Nuestra simulación debe proceder del siguiente modo:

A medida que las personas ingresan al ascensor de a una a la vez, se registra el peso de la persona.
Supondremos que el ingreso de 0 kg, indica que no hay más personas por subir al ascensor.

Si en un determinado momento del ingreso de las personas, se supera el peso máximo,
el ascensor, advertirá mediante un - mensaje, que indique que se ha excedido el peso máximo y nuestra simulación terminará.

De igual modo, si el ascensor detecta que ha subido una séptima persona al ascensor, deberá advertir de esto,
y nuestra simulación terminará.

Por último, si habiéndose indicado que todas las personas están abordo del ascensor
y las condiciones establecidas se cumplen, el ascensor anunciará "ascensor en movimiento".
"""

pesoMax = 400
maxPersonas = 6

while pesoMax >= 0 and maxPersonas >= 0:
    entran = float(input('Peso de la persona: '))
    maxPersonas -= 1
    pesoMax -= entran
    print('Una persona subio al ascensor (total: ', 6 - maxPersonas, ' personas y ', 400 - pesoMax,'kg)')

    if pesoMax <= 0:
        print('Se ha sobrepasado el peso maximo del ascensor!')
        break
    elif maxPersonas <= 0:
        print('Se ha llegado al numero maximo de personas!')
        break
    else:
        print('Sin sobrepasar maximos! Cantinuando')
