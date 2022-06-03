from io import open
import urllib.request
from bs4 import BeautifulSoup
#from nbformat import read
datos = urllib.request.urlopen('https://www.facebook.com/').read().decode()
soup = BeautifulSoup(datos)
tags = soup('//*[@id="jsc_c_66"]/div/div/span/div[1]')
#archivo = open("python\contenedor.txt", "w")
for tag in tags:
  print(tag)
  #archivo.write(tag.text+"\n")
#archivo.close()