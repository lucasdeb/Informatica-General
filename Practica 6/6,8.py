def main():
    lst = []
    n = int(input())
    while n != 0:
        if n not in lst:
            insertOrd(lst,n)
            n = int(input())
    print(lst)
        
def insertOrd(lst,n):
    cont = 0
    bandera = False
    while (bandera == False):
        if lst == []:
            lst.append(n)
            bandera = True
        elif (n > lst[cont]):
            cont += 1
        else:
            lst.insert(cont,n)
            bandera = True
    return lst

main()