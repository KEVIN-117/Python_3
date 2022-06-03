from matplotlib import markers
import matplotlib.pyplot as  plt
import numpy as np

x=np.linspace(-1,5,20)
def f(x):
    return np.exp(-x**2)

plt.figure(figsize=(10,5))
plt.title("Grrafica")
plt.xlabel("Eje x")
plt.ylabel("eje y")
plt.axis((-1,5,-0.5,2))
plt.plot(x, f(x),
         marker = 'o',
         linewidth = 6, #Aumentar el tamaño de la línea
         color = 'r',
         alpha = 0.8, #Tonalidad de la línea
         markersize=15,
         linestyle = '--',
         label = 'f(x)')
plt.legend()
plt.show()
