def porc():
    porc = float(input("Ingrese el porcentaje: "))
    num = float(input("Ingrese el numero: "))
    
    while porc <= 0 or num <= 0:
        print("Error ingrese un numero mayor a 0")
        porc = float(input("Ingrese el porcentaje: "))
        num = float(input("Ingrese el numero: "))
    n = (num*porc)/100
    
    print("El {}% de {} = {}".format(porc,num,n))
porc()
