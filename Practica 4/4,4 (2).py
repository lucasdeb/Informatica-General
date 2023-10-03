def main():
    n = int(input("Ingrese un numero entero positivo: "))
    if validar(n) == True:
        print("El numero es Perfecto!")
    else:
        print("El numero no es perfecto!")
    cont = 0
    n = 0
    print("Los primeros 4 perfectos son: ")
    while cont < 4:
        n += 1
        if validar(n) == True:
            cont += 1
            print(n,end="\t")
            
def validar(n):
    s = 0
    for i in range(1,n):
        if n % i == 0 and i != n:
            s += i
    if s == n:
        return True
    else:
        return False
main()
        