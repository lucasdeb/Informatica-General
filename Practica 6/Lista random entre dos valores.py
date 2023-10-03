import random
def main():
    a = int(input("Ingresar limite del rango: "))
    b = int(input("Ingresar limite del rango: "))
    can = int(input("Ingresar cantidad de numeros en lista: "))
    lst = lstrandom(a,b,can)
    print(lst)
    print("El Valor maximo es:",maxVal(lst))
    print("El Valor minimo es:",minVal(lst))
def lstrandom(a,b,can):
    cont = 0
    lst = []
    if a > b:
        while cont != can:
            n = random.randint(b,a)
            lst.append(n)
            cont += 1
    elif b > a:
        while cont != can:
            n = random.randint(a,b)
            lst.append(n)
            cont += 1
    else:
        while cont != can:
            n = random.randint(a,b)
            lst.append(n)
            cont += 1
    return lst

def maxVal(lst):
    if lst == []:
        return None
    if lst != []:
        maxv = lst[0]
        cont = 1
        while cont != len(lst):
            if lst[cont] > maxv:
                maxv = 0
                maxv += lst[cont]
                cont += 1
            else:
                cont += 1
    return maxv
def minVal(lst):
    if lst == []:
        return None
    if lst != []:
        minv = lst[0]
        cont = 1
        while cont != len(lst):
            if lst[cont] < minv:
                minv = 0
                minv += lst[cont]
                cont += 1
            else:
                cont += 1
    return minv
        
main()