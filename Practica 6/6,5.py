import random
def main():
    lst = []
    n = int(input("Ingrese un numero entero positivo, y 0 para terminar: "))
    while n != 0:
        if ((validar(n)) == True):
            if ((estaEnLista(n,lst)) == False):
                lst.append(n)
                n = int(input())
            else:
                print("Error, numero repetido")
                n = int(input())
        else:
            print("Error, numero NO positivo")
            n = int(input())
    print("La lista generada es: ")
    print(lst)
    a = int(input("Ingrese extremo: "))
    b = int(input("Ingrese extremo: "))
    print("La lista modificada es: ")
    print(cambiaLista(a,b,lst))
def estaEnLista(n,lst):
    return int(n) in lst

def validar(n):
    if n>0:
        return True
    else:
        return False

def cambiaLista(a,b,lst):
    cont = 0
    lst1 = lst
    if a > b:
        while cont != len(lst1):
            if (b>lst1[cont]) or (a<lst1[cont]):
                n = random.randint(b,a)
                lst1[cont] = n
                cont += 1
            else:
                cont += 1
    if b > a:
        while cont != len(lst1):
            if (a>lst1[cont]) or (b<lst1[cont]):
                n = random.randint(a,b)
                lst1[cont] = n
                cont += 1
            else:
                cont += 1
    return lst1
main()