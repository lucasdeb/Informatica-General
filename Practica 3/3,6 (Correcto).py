def main():
    n = int(input("Ingrese un numero positivo: "))
    
    if validar(n) == True:
        print("Correcto!")
    else:
        print("Incorrecto!")

def validar(n):
    if n % 2 == 0:
        n2 = int(input("Ingrese un numero menor que {}: ".format(n)))
        if n2<n:
            return True
        else:
            return False
    else:
        n2 = int(input("Ingrese un numero mayor que {}: ".format(n)))
        if n2>n:
            return True
        else:
            return False
main()