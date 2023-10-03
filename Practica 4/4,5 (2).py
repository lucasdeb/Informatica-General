def main():
    n = int(input("Ingrese un numero de 4 cifras: "))
    while n<1000 or n>9999:
        n = int(input("Ingrese un numero de 4 cifras: "))
    if validar(n) == True:
        print("Cumple")
    else:
        print("No cumple")
    n = 1000
    while n <= 9999:
        if validar(n) == True:
            print(n,end="\t")
            n += 1
        else:
            n += 1

def validar(n):
    uni = n%10
    dec = n//10%10
    cent = n//100%10
    mil = n//1000
    if uni + cent == dec + mil:
        return True
    else:
        return False
main()
    