def main():
    archivo1 = open( "/Users/lucasdebarbieri/Desktop/7,1.txt","r")
    cont = 0
    maximo = 0
    minimo = 0
    total = 0
    cont1 = 0
    for i in archivo1:
        if (i == "\n"):
            cont += 1
        else:
            total += int(i)
            cont1 += 1
            cont += 1
            if maximo == 0:
                maximo = int(i)
            if minimo == 0:
                minimo = int(i)
            if int(i) > maximo:
                maximo = int(i)
            elif int(i) < minimo:
                minimo = int(i)
    prom = total/cont1
    print("El valor maximo es {}, el valor minimo es {}, el promedio es {:.2f}, la cantidad de cifras es {}".format(maximo,minimo,prom,cont))
    archivo1.close()
main()