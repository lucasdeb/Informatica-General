def main():
    num = int(input("Ingrese Numero: "))
    val1 = int(input("Ingrese Valor 1: "))
    val2 = int(input("Ingrese Valor 2: "))
    if validarP(num,val1,val2) == True:
        print(True)
    else:
        print(False)
    
def validarP(num,val1,val2):
    if val1<val2:
        if (val1>=num or num>=val2) and ((num%2!=0 or num ==2) and (num%3!=0 or num == 3) and (num%5!=0 or num ==5)):
            return True
        else:
            return False
    elif val2<val1:
        if (val1<=num or num<=val2) and ((num%2!=0 or num ==2) and (num%3!=0 or num == 3) and (num%5!=0 or num ==5)):
            return True
        else:
            return False
main()