def main():
    n = int(input("Ingrese n: "))
    x = int(input("Ingrese x: "))
    f = calc(x,n)
    print(f)
    
def calc(x,n):
    cont = 0
    a = 1
    c = 1
    f = 0
    contador = 0
    q = 1
    while n%(10**q)//(10**(q-1)) != 0:
        q += 1
        contador += 1
    
    
    while cont != contador*2:
        while x%(10**c)//(10**(c-1)) != 0 and cont%2 == 0:
            n1 = x%(10**c)//(10**(c-1))
            if cont == 0:
                f += n1
            if cont != 0:
                n3 = n1*(10**cont)
                f += n3
            c += 1
            cont += 1
        while n%(10**a)//(10**(a-1)) != 0 and cont%2 != 0:
            n2 = n%(10**a)//(10**(a-1))
            if cont == 0:
                f += n2
            if cont != 0:
                n4 = n2*(10**cont)
                f += n4
            a += 1
            cont += 1
    return f
main()