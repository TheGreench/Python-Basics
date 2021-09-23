n = int(input('Ingrese un numero: '))
m = int(input('Ingrese otro numero: '))

if n > m:
  print(f'El primer numero {n}  es mayor que el segundo {m}')
elif n < m:
  print(f'El segundo numero {m}  es mayor que el primero {n}')
else:
  print('Los numeros son iguales')
