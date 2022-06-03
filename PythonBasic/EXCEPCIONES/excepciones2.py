def divide():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese un numero: "))
        print(f"El resultado es: {num1 // num2}")
    except ValueError:
        print("El valor introducido es incorrecto")
    except ZeroDivisionError:
        print("El resutado es indeterminado")
    finally:
        print("EL PROGRAMA A FINALIZADO")  
divide()