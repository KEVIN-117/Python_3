# LA HERENCIA
  # que es ?: se trata de trasladar el comportamiento de la herencia entre personas que ocurre en la vida real a codigo de programacion
#para que sirve?: para reutilizar codigo en caso de crear objetos similares.
                #      
class Vehiculos():
    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print(f"Marca:{self.marca} \nModelo:{self.modelo} \nEn Marcha:{self.enmarcha} \nAcelera:{self.acelera} \nFrena:{self.frena}")
class Moto(Vehiculos):
    pass

miMoto=Moto("Honda", "CBR")
miMoto.estado()