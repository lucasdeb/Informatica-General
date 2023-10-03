def main():
    n = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    n3 = int(input("Ingrese el tercer numero: "))
    
    if n>n2>n3:
        print("{} {} {}".format(n3,n2,n))
    if n2>n>n3:
        print("{} {} {}".format(n3,n,n2))
    if n>n3>n2:
        print("{} {} {}".format(n2,n3,n))
    if n2>n3>n:
        print("{} {} {}".format(n,n3,n2))
    if n3>n>n2:
        print("{} {} {}".format(n2,n,n3))
    if n3>n2>n:
        print("{} {} {}".format(n,n2,n3))
main()