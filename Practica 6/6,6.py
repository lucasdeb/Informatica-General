def main():
    print("La lista cargada es: ")
    lst = cargarlista()
    print("La lista ordernada es: ")
    print(ordernar(lst))
def cargarlista():
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
    return lst
def estaEnLista(n,lst):
    return int(n) in lst

def validar(n):
    if n>0:
        return True
    else:
        return False
    
def ordernar(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

            
    return lst
main()