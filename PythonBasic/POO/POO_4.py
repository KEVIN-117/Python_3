#Traslado a codigo los conceptos de la POO 
#veremos como crear una segunda instancia un segundo objeto que pertenese a la misma clase y como estos objetos tienen caracteristicas en comun pero 
# son objetos diferentes

class coche():
    def __init__(self): # ESTO ES UN CONTRUCTOR ASI SE CREA UN CONTRUCTOR

        self.largoChasis = 250   #|<> ESTADO INICIAL SE LE ESPECIFICA CON UN CONSTRUCTOR UN CONSTRUCTOR ES UN METODO ESPECIAL,QUE LE DA ESTADO INICIAL,A LOS OBJETOS
        self.anchoChasis = 120   #|      
        self.ruedas      = 4     #| |<> #nuestra clase coche tiene 4 propiedades
        self.enmarcha    = False#/--|
    
    def arrancar(self,arrancamos):  #def  Method un metodo es una funcion especial
        self.enmarcha = arrancamos
        if (self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        print(f"El coche tiene: {self.ruedas}, ruedas. Un ancho de {self.anchoChasis}, y un largo de {self.largoChasis}")

miCoche = coche() #CREACION DE LA PRIMERA INSTANCIA| a esto se le llama instanciar una clase


#print(f"El largo del coche es: {miCoche.largoChasis}")
#print(f"El coche tiene {miCoche.ruedas} ruedas")
print(miCoche.arrancar(True)) # LE DECIMOS QUE ARRANQUE

miCoche.estado() # LE PREGUNTA EL ESTADO




print("-------------A CONTINUACION CREAMOS EL SEGUNDO OBJETO---------------")

miCoche2 = coche()  #CREACIONN DE LA SEGUNDA INSTANCIA

#print(f"El largo del coche es: {miCoche2.largoChasis}")
#print(f"El coche tiene {miCoche2.ruedas} ruedas")
print(miCoche2.arrancar(False)) #LE DECIMOS QUE NO ARRANQUE

miCoche2.estado() #LE PREGUNTA EL ESTADO