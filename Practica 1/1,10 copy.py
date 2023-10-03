def main():
    n = int(input("Ingrese un numero binario: "))
    nstr = str(n)
    nlen = len(nstr)
    x = 0
    p = nlen - 1
    n4 = 0
    while nlen != x:
        n1 = nstr[x]
        n2 = int(n1)
        n3 = (2**p)*n2
        n4 += n3
        x += 1
        p -= 1
    print("El numero binario en base 10 es: {}".format(n4))
main()