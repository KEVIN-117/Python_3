mySet = {"Kevin", "alexis", "rodriguez", "Condori"}
#using methods in set
print("method add()")
mySet.add("newElement")
print(mySet)

print("method clear()")
set2 = mySet.copy()
set2.add("elements")
print("Set 2")
print(set2)

set3 = set2.copy()


print("method diferense()")
dif = set2.difference(mySet)
print(dif)

print("method diferense_update()")
set2.difference_update(mySet)
print(set2)

print("method discard()")
print(set3)
set3.discard("elements")
print(set3)

print("method intersection()")
print(f"set2 {set2}")
print(f"set 3 {set3}")
intersec = set3.intersection(set2)
print(intersec)

print("method intersection_update()")
mySet.pop()
print(f"myset {mySet}")
print(f"set 3 {set3}")
set3.intersection_update(mySet)
print(set3)

print("method isdisjoint()")

print(f"set2 {set2}")
print(f"set 3 {set3}")
M = set3.isdisjoint(set2)
print(M)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)

print(z)

print("method clear()")
mySet.clear()
print(mySet)