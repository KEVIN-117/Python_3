A = ['kevin', '25', 'alexis', '456', 'Rodriguez']
newList = ['kevin', 'alexis', 'Rodriguez']
"""for i in A:
    if 'e' in i:
        newList.append(i)
        A.remove(i)
print(A)

printMethod = [i.upper() for i in A if 'e' in i]
print(printMethod)"""
A.sort()
A.extend(newList)
print(A)
A.append('new element in yhe final')
print(A)
A.insert(2, 'I am new Element')
A.remove('kevin')
print(A)
A.remove('kevin')
print(A)
print(A.count('kevin'))
#[print(A[i]) for i in range(0, len(A))]
