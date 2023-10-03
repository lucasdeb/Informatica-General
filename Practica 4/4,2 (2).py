def main():
    n = int(input("Ingrese numeros enteros positivos (finalice con 0): "))
    may = 0
    men = 0
    while n != 0:
        if n > may:
            may = 0
            may += n
        if n < men:
            men = 0
            men += n
        n = int(input())
    print("El mayor es: {} y el menor es: {}".format(may,men))
main()
    
        