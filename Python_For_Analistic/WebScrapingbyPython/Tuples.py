#Tuples in python
myTuple = ("Kevin", "Alexis", "Rodriguez", "Condori")
#Type og the Tuple
print(type(myTuple))
#Indexing in tuples
print(myTuple)
print(myTuple[2:len(myTuple)])#Access elemnt of the tuple

name = 'Kevin'
if name in myTuple:
    print(f"my name is {name.upper()}")
else:
    print(f"{name} is not  in the tuple")


#Update in tuples
convertTupleinList = list(myTuple)# using the list builder for convert myTuple to list
print(type(convertTupleinList))
convertTupleinList.append("21 years old")#append new element in the list
myTuple = tuple(convertTupleinList) # using the tupple builder
print(myTuple)



try:
    myTuple2 = tuple(convertTupleinList)
    del myTuple2  # to the moment of using del delete everything data in the tuple and the variable not exist and present
    # a error in the code
    print(myTuple2)
except:
    print("the variable myTuple2 has been delete")

#unpacking a  tuples
(name, secondName, lastName, secondLastName, age) = myTuple # asigned the elements of the tuple a diferents variables
print(name)
print(secondName)
print(lastName)
print(secondLastName)
print(age)


print("\n\n")
#using * expression when there are many elements in the tuple they are assigned to a variable and it
    # will be a variable of type list
(name, secondName, *lastName) = myTuple# asigned the elements of the tuple a diferents variables
print(type(name), name)
print(type(secondName) , secondName)
print(type(lastName), lastName)

print("\n\n")
#using * expression when there are many elements in the tuple they are assigned to a variable and it
    # will be a variable of type list
(name, *secondName, lastName) = myTuple# asigned the elements of the tuple a diferents variables
print(type(name), name)
print(type(secondName), secondName)
print(type(lastName), lastName)


print("\n\ntraversal of a tuple with loops")
#traversal of a tuple with loops

print("with loop for")
#with loop for
for i in myTuple:
    print(i)

#with loop for with index
print("\nwith loop for with index")
for i in range(len(myTuple)):
    print(myTuple[i])


print("\n\nwith loop while")
# with loop while
i = 0
while i < len(myTuple):
  print(myTuple[i])
  i = i + 1



print("\n\nMethods of the tuples")
convertTupleinList.append(convertTupleinList[1])
tuple2 = tuple(convertTupleinList)
#using Method count()
print(f"the element {convertTupleinList[1]} is repeated {tuple2.count(convertTupleinList[1])} times")

#using Method index()
print(f"the element {convertTupleinList[1]} is in the {tuple2.index(convertTupleinList[1])} index")