def main():
    
    print("La lista contiene:",cargarlista())
    
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
    
main()