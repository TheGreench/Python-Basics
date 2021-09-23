dia = int(input('Ingrese numero del dia: '))
mes = int(input('Ingrese numero del mes: '))
anio = int(input('Ingrese numero del año: '))

res = dia

for i in range(1, mes):
  if i==1 or i==3 or i==5 or i==7 or i==8 or i==10:
    res = res + 31
    # It wiuld be elif - teacher wanted this
  else:
    if i==2 or i==4 or i==6 or i==9:
      res = res + 30
    else:
      if anio % 4 == 0:
        res = res + 29
      else:
        res = res + 28

print(f'Numero del año: {res}')
