#nota_1 = int(input())
#nota_2 = int(input())
#nota_3 = int(input())
#
#notaFinal = (nota_1*0.15+nota_2*0.35+nota_3*0.5)/3
#print(round(notaFinal, 2))
#nombre = input("¿Como te llamas? ")
#print(nombre.upper(), "\nTiene ",len(nombre) , " letras")

#from dataclasses import replace
#
#
#
#import re, string
#t = '¿En dónde trabajas?, ¿CUÁNTA EXPERIENCIA TIENES?, ¿Por qué has tenido 5 trabajos en solo 2 años?.'
#replace =  re.sub('[%s]' % re.escape(string.punctuation), ' ', t)
#print(replace)
#t = '¿En dónde trabajas?, ¿CUÁNTA EXPERIENCIA TIENES?, ¿Por qué has tenido 5 trabajos en solo 2 años?.'
#caracteres = "¿?!#$%^&*(),;"
#for i in caracteres:
#    t = t.replace(i, '')
#print(t.lower(), "tiene " , len(t) , " caracteres")

#from re import A
#cadena = "zeréP epeP,81"
#A,B = cadena.split(",");
#print(A[::-1], " a sacado un ", B[::-1], " de nota" )

#nombre="Nataly Silva"
#edad= 18
#direccion= "Av. República de Panamá 3055"
#pais= "Perú"
#ingreso= 3500
#gastos= 1820.50
#print(f"'{nombre}, de {edad} años y domicilio en {direccion} {pais}, tiene restante de su ingresos tras los gastos {round(ingreso-gastos, 2)}'")

#Dividendo = int(input("Ingrese el Dividendo: "))
#Divisor = int(input("Ingrese el Divisor: "))
#if(Divisor == 0):
#    print("ERROR ¡No se puede dividir entre cero! ")
#else:
#    print(Dividendo/Divisor)

#suma = 0
#sumaImpares = 0;
#for i in range(1, 100):
#    suma += i
#    if(i%2==0):
#        sumaImpares += i
#print(suma)
#print(sumaImpares)


#try:
#    numero = int(input("Digite un numero: "))
#    if(numero>=1 and numero <=10 ):
#        for i in range(0,11):
#            print(f"{numero} * {i} = {numero*i}")
#    else:
#        if(numero <0):
#            print(f"El numero {numero} debe ser mayor a -1")
#        elif(numero > 10):
#             print(f"El numero {numero} debe ser menor o igual a 10")
#except:
#    print("ERROR ¡Debe ingresar un numero!")


#password = "PASSWORD"
#passwordPrueba = ""
#esDiferente = True
#while(esDiferente):
#    if(passwordPrueba == password.upper() or passwordPrueba == password.lower()):
#        print("Contraceña correcta")
#        esDiferente = False
#    else:
#        passwordPrueba = input("Introduce la comntraceña: ")


#numeros = []
#for i in range(0,6):
#    numero = int(input("Ingrese un numero: "))
#    numeros.append(numero)
#numeros2 = []
#numeros2.append(numeros[len(numeros)-1])
#numeros.remove(numeros[len(numeros)-1])
#numeros2.append(numeros[len(numeros)-1])
#numeros.remove(numeros[len(numeros)-1])
##Imprimir lista
#numeros2.extend(numeros)
#print(f"Los numeros ingresados son {numeros2}")


#letras = {'a','b','c','d','e','f', 'g', 'h','i'}
#vocales = {'a','e','i','o','u'}
#U = letras.union(vocales)
#I = letras.intersection(vocales)
#D = letras.difference(vocales)
#print(U)
#print(I)
#print(D)


#SetNumeros1 = {1,2,3,4,5,6,7,8,9}
#SetNumeros2 = {1,3,5,7,9}
#U = SetNumeros1.union(SetNumeros2)
#I = SetNumeros1.intersection(SetNumeros2)
#D = SetNumeros1.difference(SetNumeros2)
#print(U)
#print(I)
#print(D)

#palabra = input("Ingrese una plabra: ")
#
#listOfVocals = ['a','e','i','o','u']
#for i in listOfVocals:
#    palabra = palabra.replace(i, '')
#Mylist =  list(palabra.upper())
#Mylist.sort()
#Mylist.reverse()
#print(Mylist)

Fruits = {
    "platano":1.35,
    "Manzana":0.80,
    "Pera":0.85,
    "Naranja":0.70
}
optionSelectionFruit = input("¿Que elegira?: ")
numberOfKilos = float(input("Digite la cantidad que desea en Kilos: "))
if(Fruits.keys() == optionSelectionFruit ):
    print("No quedan mas unidades de la fruta que selecciono ")
else:
    print(Fruits.items(optionSelectionFruit))
    
