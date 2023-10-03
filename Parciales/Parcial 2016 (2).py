def main():
    n = int(input("[Primero]: "))
    paridad(n)

def paridad(n):
    par = 0
    impar = 0
    mal = 0
    if n%2==0:
        es_par = True
    else:
        es_par = False
    while n != 0:
        if es_par == True:
            par += 1
            n = int(input("[Impar]: "))
            while (n%2 == 0) and (n!=0) and (n != " "):
                mal += 1
                n = int(input("Re-Ingreso[Impar]: "))
            es_par = False
        else:
            impar += 1
            n = int(input("[Par]: "))
            while (n%2 != 0) and (n!=0) and (n != " "):
                mal += 1
                n = int(input("Re-Ingreso[Par]: "))
            es_par = True
    print("Se Ingresaron: ")
    print("Pares: {}".format(par))
    print("Impares: {}".format(impar))
    print("Paridad Incorrecta: {}".format(mal))
main()