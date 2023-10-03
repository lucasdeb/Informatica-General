def main():
    n1 = int(input("Ingrese primer numero: "))
    n2 = int(input("Ingrese segundo numero: "))
    n3 = int(input("Ingrese tercer numero: "))
    
    n = n1+n2+n3
    
    if n1 < 0:
        print("-{:>10}".format(n1*(-1)))
    else:
        print("{:>10}".format(n1))
    
    print(" ")
    
    if n2 < 0:
        print("-{:>10}".format(n2*(-1)))
    else:
        print("{:>10}".format(n2))
    
    print(" ")
    
    if n3 < 0:
        print("{:>10}".format(n3*(-1)))
    else:
        print("{:>10}".format(n3))
    
    print(" ")
    
    print("- - - - - - -")
    
    print(" ")
    
    print("{:>10}".format(n))
    
main()