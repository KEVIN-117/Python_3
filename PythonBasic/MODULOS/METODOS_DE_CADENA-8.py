#Uso de metodos de cadenas.
#String: upper():la funcion convierte en mayusculas todas las letras de un String.
       # lower():la funcion convierte mayusculas a minusculas 
       # capitalize():la funcion convierte la primera letra de un string a mayucula
       # count(): este metodo sirve para contar cuantas veces aparece una letra o cadena dentro de una frase
       # find(): sirve para representar el indice o la posicion que se encuentra un caracter dentro de un texto de adelante
       # isdigit():debuelve un booleano True o False
       # isalnum():comprueba si son numeros
       # isalpha():lo que hace es comprobar si hay solo letras
       # split():separa utilizando espacios
       # strip():borra los espacios que sobran al inicio y al final
       # replace():cambia una palabra por otra dentro de un string
       # rfind():sirve para representar el indice o la posicion que se encuentra un caracter dentro de un texto de atras

nombreUsuario=input("Introduce nombre: ")
print("-------------------------------------------------PRUEBA CON upper---------------------")
print(f"El nombre es: {nombreUsuario.upper()}")
print("-------------------------------------------------PRUEBA CON lower---------------------")
print(f"El nombre es: {nombreUsuario.lower()}")
print("-------------------------------------------------PRUEBA CON capitalize---------------------")
print(f"El nombre es: {nombreUsuario.capitalize()}")
print("-------------------------------------------------PRUEBA CON split---------------------")
print(f"El nombre es: {nombreUsuario.split()}")

print("-------------------------------------------------PRUEBA CON EDAD---------------------")
Edad=input("Introduce edad: ")
print(f"La edad es: {Edad.isdigit()}")

print("-------------------------------------------------PRUEBA CON CONDICIONALES---------------------")
Edad=input("Introduce: ")
while(Edad.isdigit()==False):
    print("Introduce un valor numerico")
    Edad=input("Introduce edad: ")
if(int(Edad)<18):
    print("No puede pasar")
else:
    print("Puede pasar")



print("-----------------------------------------EJERCICIO-----------------------------------------")
