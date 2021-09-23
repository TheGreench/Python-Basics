n = 1
while n >= 0:
  n = int(input('Ingrese un numero: '))
  for i in range(n + 1):
    factorial = 1
      for j in range(1, i + 1):
        factorial = factorial * j
       if n >= 0:
          print(factorial)
