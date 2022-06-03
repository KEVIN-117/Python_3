
from datetime import datetime
today = datetime.today()
amountDays = 10000
convertToYearsandMonth = round(amountDays/365, 1)
years, month = str(convertToYearsandMonth).split(".")

FutureYear = today.year+int(years)

#Month condicional 
futureMonth = today.month+int(month)
#la siguiente fguncion retornara el futureMonth. si es > 12 cambiara la variable  sino se mantedra su valor
def returnNewMonth(futureMonth):
    saveFutureMonth = futureMonth
    if(futureMonth > 12):
        futureMonth = saveFutureMonth-12

        return futureMonth
    else:
        return futureMonth

futureDay = today.day+amountDays-(int(years)*365+int(month)*30)
def returnNewDay(futureDay):
    aux = futureDay
    if(futureDay > 30 or futureDay > 31):
        if(newfutureMonth == 2):#Este condicional es para el mes de febrero
            futureDay = aux-28
            return futureDay
        elif(newfutureMonth%2 != 0 or newfutureMonth == 12): #para los meses enero, marzo mayo julio septiembre noviembre diciembre tienen 31 dias
            futureDay = aux-31
            return futureDay
        elif(newfutureMonth%2 == 0):#para los meses  abril junio agosto octubre tienen 30 dias
            futureDay = aux-30
            return futureDay
    else:
        return futureDay


def returnNewMonthRespectDay(futureDay, futureMonth):
    #esta funcion lo que hace es cambiar el me con respecto al dia si el dia es nayor a 30 o 31 
    # entonces el dia cambiara y el mes tambien es decir aumnentara en una unidad
    aux = futureDay
    if(futureDay > 30 or futureDay > 31):
        if(futureMonth == 2):
            futureDay = aux-28
            futureMonth += 1
            return futureMonth
        elif(futureMonth%2 != 0 or futureMonth == 12):
            futureDay = aux-31
            futureMonth += 1
            return futureMonth
        elif(futureMonth%2 == 0):
            futureDay = aux-30
            futureMonth += 1
            return futureMonth
    else:
        return futureMonth
newfutureMonth = returnNewMonthRespectDay(futureDay, futureMonth)


FutureDate = str((today.year+int(years)))+"/"+str(newfutureMonth)+"/"+str(returnNewDay(futureDay))
convertToFormatDate = datetime.strptime(FutureDate, '%Y/%m/%d')

def ExtractComponents(convertToFormatDate):
    Year = convertToFormatDate.strftime("%Y")
    Month = convertToFormatDate.strftime("%m")
    Week = convertToFormatDate.strftime("%W")
    Day = convertToFormatDate.strftime("%d")

    print(f"Año: {Year}")
    print(f"Mes: {Month}" + " = {}".format(convertToFormatDate.strftime("%b")))
    print(f"Semana: {Week}")
    print(f"Dia: {Day}" + " = {}".format(convertToFormatDate.strftime("%A")))
ExtractComponents(convertToFormatDate)


print("Dentro de 10000 dias sera el dia " + convertToFormatDate.strftime("%A") + " " + 
        convertToFormatDate.strftime("%d") + " de " + convertToFormatDate.strftime("%b") + 
        " del año " + convertToFormatDate.strftime("%Y"))