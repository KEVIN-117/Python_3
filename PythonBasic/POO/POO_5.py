#ENCAPSULACIN DE METODOS
#¿QUE ES ?
#¿PORQUE UTILIZAR LA ENCAPSULACION?
class coche():
    def __init__(self): # ESTO ES UN CONTRUCTOR ASI SE CREA UN CONTRUCTOR

        self.__largoChasis = 250  #|<> ENCAPSULAR PARA QUE NO SEA POSIBLE ACCEDER A LAS VARIABLES DESDE FUERA
        self.__anchoChasis = 120  #|<>ENCAPSULAR ES HACER QUE UN METODO SOLO SEA ACCESIBLE DESDE LA PROPIA CLASE Y NO SE PUEDA ACCEDER DESDE FUERA
        self.__ruedas      = 4    #|
        self.__enmarcha    = False#/
    
    def arrancar(self,arrancamos):  
        self.__enmarcha = arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
        
        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        
        elif(self.__enmarcha and chequeo==False):
            return "Algo a ido mal"
        
        else:
            return "El coche esta parado"

    def estado(self):
        print(f"El coche tiene: {self.__ruedas}, ruedas. Un ancho de {self.__anchoChasis}, y un largo de {self.__largoChasis}")
    
    def __chequeo_interno(self):
        print("realizando chequeo interno")

        self.gasolina="ok"
        #self.aceite="mal"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

miCoche = coche() #CREACION DE LA PRIMERA INSTANCIA| a esto se le llama instanciar una clase

print(miCoche.arrancar(True)) # LE DECIMOS QUE ARRANQUE

miCoche.estado() # LE PREGUNTA EL ESTADO


print("-------------A CONTINUACION CREAMOS EL SEGUNDO OBJETO---------------")

miCoche2 = coche()  #CREACIONN DE LA SEGUNDA INSTANCIA

print(miCoche2.arrancar(False))

miCoche2.estado() #LE PREGUNTA EL ESTADO
