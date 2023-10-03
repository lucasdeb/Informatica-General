def main():
    day = int(input("Ingrese dia: "))
    month = int(input("Ingrese mes: "))
    year = int(input("Ingrese anio: "))
    
    if validar(day,month,year) == True:
        print("La fecha es correcta")
    else:
        print("La fecha es incorrecta")
def validar(day,month,year):
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and 0<day<32:
        return True
    elif (month == 4 or month == 6 or month == 9 or month == 11) and 0<day<31:
        return True
    elif (month == 2) and ((year%4 == 0 and year%100 != 0) or (year%400 == 0)) and 0<day<30:
        return True
    elif (month == 2) and ((year%4 != 0 and year%100 == 0) or (year%400 != 0)) and 0<day<29:
        return True
    else:
        return False
main()