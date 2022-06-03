print("Por Favor ingrese los datos que se le piden :)")
name = input("Enter your Name: ")
SecondName = input("enter your second name: ")
lastName = input("Enter your last name: ")
secondLastName = input(f"Enter your second last name {name}: ")
date = input(f"Enter your date of birth {name}: ")
print("\n\n")

def calcularAños(date):
    a = date[6:len(date)]
    ageInActulity = 2022-int(a)
    return f'Your are **{str(ageInActulity)}** years old'


def main(name, date):
    return f'hello "{name} {SecondName} {lastName} {secondLastName}" \nyour date of birth is "{date}"'
    
    
def saludar(name):
    return f'THAT IS  ALL FOR TODAY "{name}" THANK YOU BYE BYE :)'

def deletrear(name):
    for i in name:
        print(i)
print(main(name, date))
print(calcularAños(date))
print(saludar(name))
deletrear(name)