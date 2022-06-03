#Ejercicio 2
#
#a. ¿Qué día de la semana fue el día que naciste?
from calendar import month
from datetime import date, datetime


#birthDay = input("¿Wath day of the week it was the day what you were born?: ")
print("¿Wath day of the week it was the day what you were born?")
birthDay = '17/12/2001'
convertToDate = datetime.strptime(birthDay, '%d/%m/%Y')
print("The day what i was born is {}".format(convertToDate.strftime("%A")))


#b. ¿Cuántos días han pasado desde ese día al día de hoy?
print("¿How many days have passed from that day to today?")
yearBirth = int(convertToDate.strftime("%Y"))
thisYear = int(datetime.today().year)
dayAddition = 365*(thisYear-yearBirth)
print("The days that have passed since the day I was born is {} days".format(dayAddition) )


#c. ¿Qué día de la semana será tu cumpleaños dentro de un año?
print("¿What day of the week will your birthday be in a year?")
proximitiYear = thisYear+1
futureBirthday =str(convertToDate.strftime("%d")+"/"+convertToDate.strftime("%m")+"/"+str(proximitiYear))
convertToDate2 = datetime.strptime(futureBirthday, '%d/%m/%Y')
print("in a year my birthday will be: {}".format(convertToDate2.strftime("%A")))


