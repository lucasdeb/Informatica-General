def main():
    p = 0
    d = 0
    while p!=5:
        n = int(input("Ingrese un numero entero: "))
        if n%2 == 0 and n%4 == 0:
            p += 1
            d +=1
            print("Numero par. Numero es multiplo de 4. Total de numeros pares: {}, Total de numeros divisibles por 4: {}".format(p,d))
        if n%2 == 0 and n%4 != 0:
            p += 1
            print("Numero par. Total de numeros pares: {}, Total de numeros divisibles por 4: {}".format(p,d))
    print("/n FIN")
main()