# ¿Que es P.O.D? Es  Programacion orientada a procedimientos                
#              son los lenguajes antiguos                           
#          Programacion orientada a procedimientos                  
# Algunos ejemplos de lenguajes: Fortran, Cobol, Basic, etc         
#             ventajas  y desventajas ?                             
# Desventajas unidades de codigo muy grandes y complejas            
# En aplicaciones comlejas el codigo resulta dificil de decifrar    
# Poco reutilizable                                                 
# Si existe un error en alguna linea todo el programa caera         
# Aparicion frecuente de codigo ESPAGUETI                           
# Dicil de depurar por otros programadores                          
#¿QUE ES P.O.O? P.O.O es programacion orientada a objetos 
#              son los lenguajes modernos 
# Progrmacion Orientada a Objetos.- Esto consiste en trasladar el 
#  comporatamiento de los objetos de la vida real al codigo de programacion
#  los objetos de la vida real tienen un estado, un comportamiento, que puede  
# hacer y tanbien propiedades ejemplo : el objeto coche 
#¿Cual es su estado? Un coche puede estar parado circulando aparcado etc
#¿Que propiedades tiene? Un coche tiene un color, peso, tamaño, etc.
#¿Que comportamiento tiene? Un coche puede arrancar,frenar,acelerar,girar,etc
#    propiedades en progrmacion es atributos:
# P.O.O  ej. C++,Java,Visual.NET,etc
#Ventajas 
#El programa se puede dividir en trozoz,partes,modulos o clases = modularizacion                                                                   
# El programa es reutilizable .para reutilizar es util el concepto de Herencia                                                                    
#Si existe un fallo en alguna linea de codigo,el programa continuara con su                                                                     
# funcionamiento . a esto se le llama Tratamiento de Excepciones                                                                    
#Encapsulamient                                                                   
#Vocabulario de la POO                                                                    
#Coceptos o terminos de la POO 
#clase,Objeto,Ejemplar de clase Instancia de clase.Ejemplarizar una clase Instanciar una clase. Modularizacion,Encapsulamiento,herencia,polimorfismo.
#  obejeto = Accediendo a propiedades de objeo desde codigo (pseudocodigo)
#para acccder a propiedades y comporatamiento de objeto es por medio de la nomenclatura del punto
#objeto:
# accediendo a propiedades de objeto desde codigo(pseudocodigo):
    #miCoche.color="rojo";
    #miCoche.peso=1500;
# accediendo a comporatmiento de objeto desde codigo(pseudocodigo):
    # miCoche.arranca();
    # miCoche.frena();
# CODIGO
# TRASLADO A CODIGO LOS CONCEPTOAS DE LA POO VISTOS ANTERIORMENTE 
class coche():
    largoChasis = 250
    anchoChasis = 120      #nuestra clase coche tiene 4 propiedades
    ruedas      = 4
    enmarcha    = False
    def arrancar(self):  #def  Method un metodo es una funcion especial
        self.enmarcha = True
    
    def estado(self):
        if (self.enmarcha):
            return "El coche esta en marcha"
        else: 
            return "El coche esta parado "

miCoche = coche() # a esto se le llama instanciar una clase

print(f"El largo del coche es: {miCoche.largoChasis}")
print(f"El coche tiene {miCoche.ruedas} ruedas")
miCoche.arrancar()
print(miCoche.estado())

print("-------------A CONTINUACION CREAMOS EL SEGUNDO OBJETO-----------")
#Traslado a codigo los conceptos de la POO 
#veremos como crear una segunda instancia un segundo objeto que pertenese a la misma clase y como estos objetos tienen caracteristicas en comun pero 
# son objetos diferentes
miCoche2 = coche()
print(f"El largo del coche es: {miCoche2.largoChasis}")
print(f"El coche tiene {miCoche2.ruedas} ruedas")
print(miCoche2.estado())