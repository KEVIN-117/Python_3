def first():
    print("Hello this is a function without parameters")

def last(name):
    print(f"Hello my name is {name}, and this is a function with parameters")


def undefined(*parameters):
    print("hello this is a function with a number undefined of parameters")
    counter = 0
    for i in parameters:
        counter += 1
        print(f"{str(counter)} : parameter in the function " , i)


def functionWithArgumrnts(firstName, LastName, age):
    print(f"this is a function with arguments and keywords \nHello My name is {firstName}{LastName} and i am {age} years old")


def functionDictyonariKeywords(**key):#estructure key:value
    counter =0
    print(key, "\n")
    for i in key:
        counter += 1
        print(str(counter), key[i])

def defaultParametersValue(name="", country=""):
    print(f"my name is {name} and I am from of {country}")


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


first()
last("KEVIN")
undefined("KEVIN", "ALEXIS", "RODRIGUEZ", "CONDORI", 24)
functionWithArgumrnts(firstName="Kevin", LastName="Rodriguez", age=21)
functionDictyonariKeywords(fname = "Kevin", sName="Alexis", lName = "Rodriguez", lSName="Condori", birth="17 de diciembre de 2001", age= 21)
defaultParametersValue("Kevin", "Bolivia")
defaultParametersValue("Lorena", "Bolivia")
defaultParametersValue("Alexis", "Canada")
print("\nRecursion Example Results")
tri_recursion(6)