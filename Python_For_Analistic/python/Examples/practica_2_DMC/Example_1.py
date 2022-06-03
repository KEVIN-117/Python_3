#Ejercicio 1
#
#Convierta a formato fecha las siguientes cadenas: (utilice la función strptime):
#'18/02/2019'
#'01/31/2000 12:00:00AM
#%a: Nombre local abreviado de día de semana
#%A: Nombre local completo de día de semana
#%b: Nombre local abreviado de mes
#%B: Nombre local completo de mes
#%c: Representación local de fecha y hora
#%d: Día de mes [01,31]
#%p: Etiqueta AM o PM
#%I: Hora (horario 12 horas) [01,12]
#%j: Número de día del año [001,366]
#%m: Mes [01,12]
#%M: Minuto [00,59]
from datetime import datetime

A = '18/02/2019'
B = '01/31/2000 12:00:00AM'

convertA = datetime.strptime(A, '%d/%m/%Y')
convertB = datetime.strptime(B, '%m/%d/%Y %H:%M:%S%p')
print(type(convertA))
print(convertA)
print(convertB)
