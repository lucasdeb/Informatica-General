def main():
    n = int(input("Ingrese un numero natural: "))
    nstr = str(n)
    nlen = len(nstr)
    num = sacarpar(n, nlen)
    print("El numero sin pares es: {}".format(num))
def sacarpar(n, nlen):
    pot = 0
    num = 0
    c = 0
    while c != nlen:
        n1 = n%(10**(c+1))//(10**c)
        if n1%2 == 1:
            num += n1*10**pot
            pot += 1
            c += 1
        else:
            c+=1
    return num
main()
        