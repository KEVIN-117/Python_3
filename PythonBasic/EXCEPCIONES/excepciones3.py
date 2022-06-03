 #LANZAMIENTO DE EXCEPCIONES  
    #INSTRUCCION RAISE     raise = aumentar
edad = int(input("Ingresa una edad: "))
def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("AS INTRODUCIDO EDAD NEGATIVA")
    elif edad < 15:
       return "ERES UN MENOR"
    elif edad < 40:
        return "ERES MUY JOVEN"
    elif edad < 65:
        return "ERES MUY MADURO"
    elif edad <= 100:
        return "CUIDATE.."
print( evaluaEdad(edad))



import math
num1 = float(input("Ingresa un numero"))
def raiz_cuadrada(num1):
    if num1 < 0:
        raise ValueError ("no se puede hallar raises negativas")
    else:
        return math.sqrt(num1)
try:
    print(f"La raiz es:{raiz_cuadrada(num1)}")
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print("EL PROGRMA TERMINO")