def main():
    n = int(input("Ingrese numero de 5 cifras: "))
    
    n1 = (n//10000)**2
    n2 = (n//1000%10)**2
    n3 = (n//100%10)**2
    n4 = (n//10%10)**2
    n5 = (n%10)**2
    
    print("{}-{}-{}-{}-{}".format(n1,n2,n3,n4,n5))
main()