def main():
    paridad()
def paridad():
    p = 0
    i = 0
    c = 0
    n = int(input("Primero: "))
    while n != 0:
        if n%2 == 0:
            p += 1
            n = int(input("(Impar): "))
            while not n%2 != 0 and n != 0:
                p +=1
                n = int(input("Reignreso (Impar): "))
                c += 1
        else:
            i += 1
            n = int(input("(Par): "))
            while not n%2 == 0 and n != 0:
                i += 1
                n = int(input("Reignreso (Par): "))
                c += 1
            
        
    print("Se ingresaron:")
    print("Pares: {}".format(p))
    print("Impar: {}".format(i))
    print("Paridad incorrecta: {}".format(c))
main()