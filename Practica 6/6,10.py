import random
def main():
    lst = cargarlistaAlea()
    print("La lista generada es: ")
    print(lst)
    print("Hay {} en la lista".format(atributotriple(lst)))
    
def atributotriple(lst):
    trip = 0
    bandera = False
    for i in range(0,len(lst)-2):
        if (lst[i]==lst[i+1]==lst[i+2]) and (bandera == False):
            trip += 1
            bandera = True
        if ((lst[i]==lst[i+1]==lst[i+2]) == False):
            bandera = False
        if (i+1)%3==0:
            bandera = False
        
        
    """
    pos = 0
    prim = False
    while pos+2 != len(lst):
        while (lst[pos]==lst[pos+1]==lst[pos+2]) and prim == False:
            trip += 1
            pos += 1
            prim = True
        
        if (lst[pos]==lst[pos+1]==lst[pos+2]) and ((lst[pos-1]==lst[pos]==lst[pos+1])==False):
            trip += 1
            pos += 1
        elif pos+6<len(lst):
            if ((lst[pos]==lst[pos+3]) and (lst[pos+1]==lst[pos+4]) and (lst[pos+2]==lst[pos+5])):
                trip += 1
                pos += 1
        else:
            pos += 1
    """
    if trip == 0:
        return "NADA"
    if trip == 1:
        return "Un Trip"
    if trip == 2:
        return "Dos Trip"
    if trip >= 3:
        return "+ Triple"
    
def cargarlistaAlea():
    lst = []
    a = int(input())
    b = int(input())
    can = int(input())
    while a==b:
        print("Ingrese dos valores distintos de a y b")
        a = int(input())
        b = int(input())
    while (can<=3):
        print("Ingrese una cantidad mayor a 3")
        can = int(input())
    while (len(lst) != can):
        if a < b:
            lst.append(random.randrange(a,b+1))
        if b < a:
            lst.append(random.randrange(b,a+1))
    return lst

main()