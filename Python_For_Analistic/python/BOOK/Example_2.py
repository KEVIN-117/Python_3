from ctypes import addressof


name = input("Whath is your name?: ")
address = input("Whath is your address?: ")
phoneNumber = int(input("What is your phone number?: "))

def returnDates(name, address, phoneNumber):
    return f"My name is {name} \nmy address is {address} \nmy phone number is {phoneNumber}"
print(returnDates(name, address, phoneNumber))