import numpy as np

import pandas as pd

read = pd.read_csv("Salaries.csv")

print(len(read))
print(
    "<---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->")
print(read.head(5))
print(read.info())
print("<---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->")
# mean = np.sum(read[['BasePay']], axis=0)


# ¿Cuál es el promedio de BasePay?

meanBasePay = np.mean(read[['BasePay']])
print("El promedio es " + str(meanBasePay))
mean2 = np.mean(read[['BasePay']])
print("El promedio es " + str(mean2))

# ¿Cuál es la mayor cantidad de OvertimePay en el conjunto de datos?
dateMaximun = np.max(read[['OvertimePay']])
print("la mayor cantidad de OvertimePay es: " + str(dateMaximun))

# ¿Cuál es el título del trabajo de empleado (EmployeeName) JOSEPH DRISCOLL? Nota: use mayúsculas, de lo contrario, puede obtener una respuesta que no coincide (también hay una minúscula Joseph Driscoll)

SearchName = read.loc[:, 'EmployeeName'] == 'NATHANIEL FORD'
DataOfUser = read.loc[SearchName]
print(DataOfUser[['JobTitle']])

# ¿Cuánto gana JOSEPH DRISCOLL (incluidos los beneficios "TotalPayBenefits")?
print(DataOfUser[['TotalPay', 'TotalPayBenefits']])

# ¿Cuál fue el BasePay promedio (promedio) de todos los empleados por año? (2011-2014)?

year = read[(read['Year'] > 2011) & (read['Year'] < 2014)]
print(year['BasePay'].mean())

print('¿Cuántos títulos de trabajo únicos hay (use .unique())?')

unique = pd.unique(read['JobTitle'])
print(len(unique))

