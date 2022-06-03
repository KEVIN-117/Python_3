list = ['kevin', 'alexis', 'bbqcwc', 'sgbqvc', 'uhuyq', 'gywqd']
print(list)
list.append('alexis')
print(list)
list2 =list.copy()
print(list2)
print(list.count("alexis"))
list.extend(list2)
print(list,"\n", list.count("alexis"))
print(list.index("kevin"))
list.insert(0, "Perrito")
print(list, list.index("Perrito"))

list.pop(0)
print(list)

list.remove("kevin")
print(list)
list2.reverse()
print(list2)

list.sort()
print(list)