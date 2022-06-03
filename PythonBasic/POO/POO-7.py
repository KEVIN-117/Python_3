#POO-IX__POLIMORFISMO:en programacion significa que un obejeto puede cambiar de forma 
class Coche():
    def desplazamiento(self):
        print("Me desplazo en 4 ruedas")
class Moto():
    def desplazamiento(self):
        print("Me desplazo en 2 ruedas")
class Camion():
    def desplazamiento(self):
        print("Me desplazo en 6 ruedas")

miVehiculo=Moto()
miVehiculo.desplazamiento()

miVehiculo2=Coche()
miVehiculo2.desplazamiento()

miVehiculo3=Camion()
miVehiculo3.desplazamiento()


print("****************************************la magia del polimorfismo**************************")
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Camion()
desplazamientoVehiculo(miVehiculo)