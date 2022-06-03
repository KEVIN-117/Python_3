import MODULOS

MODULOS.sumar(7,5)

MODULOS.restar(9,5)

MODULOS.multiplicar(5,5)

print("otra forma de importar modulos")
from MODULOS import sumar
sumar(7,5)

from MODULOS import restar
restar(9,5)

from MODULOS import multiplicar
multiplicar(5,5)

print("otra forma de importar modulos")
from MODULOS import *
sumar(7,5)

restar(9,5)

multiplicar(5,5)