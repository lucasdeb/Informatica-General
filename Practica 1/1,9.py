def main():
    n = int(input("Ingrese numero de cantidad impar de cifras (al menos 3 cifras): "))
    nstr = str(n)
    nlen = len(nstr)
    
    first = n//10**(nlen-1)
    middle = n//10**(nlen//2)%10
    last = n%10
    
    print("El numero ingresado tiene {} cifras".format(nlen))
    print("La primera cifra es {}, la ultima es {} y la central es {}".format(first,middle,last))
main()
    
    