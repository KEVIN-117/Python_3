#Herencia II
#herencia_multiple
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
class Furgoneta(Vehiculos):
    def carga(self, carga):
        self.cargado=carga
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculos):
    hc_caballito=""
    def caballito(self):
        self.hc_caballito="Hago el caballito"
    def estado(self):
        print(f"Marca:{self.marca} \nModelo:{self.modelo} \nEn Marcha:{self.enmarcha} \nAcelera:{self.acelera} \nFrena:{self.frena} \n{self.hc_caballito}")

class vehiculosHelectricos():
    def __init__(self):
        self.autonomia=100
    def cargaEnergia(self):
        self.cargando=True
print("*********************************************************MOTO*****************************************************************")
miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

print("*******************************************************FURGONETA**************************************************************")
miFurgoneta=Furgoneta("Renault", "Kango")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BicicletaElectrica(vehiculosHelectricos, Vehiculos):#ESTO ES LA HERENCIA MULTIPLE
    pass

miBici=BicicletaElectrica("Mozo","IJ0117")