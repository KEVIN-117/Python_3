import math
import numpy as np
print(np.__version__)
#myArr = np.array([[4,5,6],
#                  [9,2,3],
#                  [9,2,3]])
#print( f"Dimencion {myArr.ndim}")
#print( f"Muestra las dimenciones del vector: {myArr.shape}")
#print( f"Numero total de elementos {myArr.size}")
#print( f"tipo de datos en el vector {myArr.dtype}")
#print( f"tamaño en bytes {myArr.itemsize}")
#
## array con datos aleatorio
#arange = np.arange(0, 20, 2)
#print(arange)
#linspace = np.linspace(0, 20, 2)
#print(linspace)

myArr1 = np.array([4,5,6])
myArr2 = np.array([9,2,3])
resultMultipli = np.multiply(myArr1, myArr2)
print(resultMultipli)
result = np.dot(myArr1, myArr2)
print(result)