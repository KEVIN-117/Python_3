#las excepciones son errores que ocurren durante la ejecucion del programa
def multiplicar(num1, num2):
    return num1 * num2
def dividir(num1, num2):
    try:        # try = intentar , intentar realizar la exprecion 
        return num1 // num2
    except ZeroDivisionError:   #try y except son como el if y else 
        print("operacion es indefinida")
        return "operacion  indefinida"
while True:
    try:
        numero = int(input("introduce el primer numero:   "))
        numero2 = int(input("introduce el segundo numero: "))
        break
    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo")
operacion = input("Introduce la operacion a realiza (multiplicar, dividir): ")
if operacion == "multiplicar":
    print("el resultado es: ", multiplicar(numero, numero2))
    

elif operacion == "dividir":
    print("el resultado es:", dividir(numero, numero2))

else:
    print("La operacion no se puede realizar")

print(" FIN DEL PROGRAMA ")
