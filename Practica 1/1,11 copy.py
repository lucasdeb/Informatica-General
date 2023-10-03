def main():
    n = int(input("Ingrese un numero de base 10 de maximo de 5 cifras: "))
    
    octal = 0
    c = 0
    p = 1
    while (n//8**c) != 0:         
        n1 = (n//8**c)%8    
        c += 1
        octal += n1*p
        p = p*10
        
    print("El numero en octal es: {}".format(octal))
    
main()