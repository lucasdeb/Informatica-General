def main():
    lst = []
    n = int(input("Ingrese un numero entero positivo, y 0 para terminar: "))
    while n != 0:
        while ((n in lst) == True) and (n!=0):
            print("Error, numero repetido")
            n = int(input())
        while ((n not in lst) == True) and (n!=0):
            lst.append(n)
            n = int(input())
    print("Lista Generada: \n",lst)
    num = int(input("Ingrese valor a insertar: "))
    
    print(insertOrd(lst,num))
    
def insertOrd(lst,num):
    cont = 0
    bandera = False
    while cont != len(lst) and (bandera == False):
        if num > lst[cont]:
            cont += 1
        else:
            lst.insert(cont,num)
            bandera = True
    return lst

main()
        