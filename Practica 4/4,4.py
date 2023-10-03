def main():
    n = int(input("Ingrese numero: "))
    if validar(n) == True:
        print("el numero es Perfecto!")
    

def validar(n):
    cont = 0
    for i in range(1,100000000):
        if n%i == 0 and cont != n:
            cont += i
    if cont == n and cont != 0:
        return True
"""
def prim(n):
    while cont1 != 4:
        if validar(n) == True:
            cont1 += 1
            print(cont)
"""       
main()
        