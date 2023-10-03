def main():
    lst = []
    num = input("Ingrese numero para encontrar: ")
    if estaEnLista2(num,lst) == True:
        print("True")
    else:
        print("False")
"""
def estaEnLista(num,lst):
    return int(num) in lst
    
def estaEnLista1(num,lst):
    cont = 0
    for i in lst:
        if int(num) == i:
            cont += 1
    if cont >= 1:
        return True
    else:
        return False
"""
def estaEnLista2(num,lst):
    cont = 0
    bandera = False
    while (cont != len(lst)) and (bandera == False):
        if lst[cont] == int(num):
            bandera = True
        else:
            cont += 1
    return bandera
        
    
main()