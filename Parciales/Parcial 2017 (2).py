def main():
    val1 = int(input("Ingresar Extremo 1: "))
    val2 = int(input("Ingresar Extremo 2: "))
    div = int(input("Ingresar divisor: "))
    while div == 0:
        div = int(input("Error. Ingresar divisor: "))
    num = int(input("Ingresar numero: "))
    while num == 0:
        num = int(input("Error. Ingresar numero: "))
    if validar(val1,val2,div,num) == True:
        print(True)
    else:
        print(False)
        
def validar(val1,val2,div,num):
    if val1 < val2:
        if (num%div==0) and (val1<=num<=val2):
            return True
        else:
            return False
    elif val1 > val2:
        if (num%div==0) and (val2<=num<=val1):
            return True
        else:
            return False
    else:
        if (num%div==0) and (val1==num==val2):
            return True
        else:
            return False
main()