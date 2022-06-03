#Herencia III
 #SE UTILIZAR 2 FUNCIONES :super(); isinstance()
#super():sirve para llamar al metodo de la clase madre o sea de la primera clase que contiene un constructor
#isinstance()
class Persona():
    def __init__(self, nombre, edad, Lugar_de_recidencia):
        self.nombre=nombre
        self.edad=edad
        self.Lugar_de_recidencia=Lugar_de_recidencia
    def descripcion(self):
        print(f"Nombre:{self.nombre} \nEdad:{self.edad} \nResidencia:{self.Lugar_de_recidencia}")

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_del_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_del_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print(f"Salario:{self.salario} \nAntiguedad:{self.antiguedad}")
print("///////////////////////////////////////////////////////PERSONA//////////////////////////////////////")
Kevin=Persona("Kevin", 19, "Bolivia")
Kevin.descripcion()
print(isinstance(Kevin,Persona))

print("*******************************************************EMPLEADO/////////////////////////////////////")
Alexis=Empleado(2000, 10, "Alexis", 19, "Bolivia")
Alexis.descripcion()
print(isinstance(Alexis,Empleado))



print("**********************************************EJEMPLO DE LA POO-6.1************************************")

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

class vehiculosHelectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
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