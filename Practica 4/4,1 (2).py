def main():
    i = 0
    while i < 5:
        n = int(input("Ingrese un numero entero: "))
        if n % 2 == 0 and n % 4 == 0:
            i += 1
            print("Numero par. Tambien es mult. de 4 Total de numeros pares ingresados: {}".format(i))
        if n%2 == 0 and n % 4 != 0:
            i += 1
            print("Numero par. Total de numeros pares ingresados: {}".format(i))
    print("\nFIN")
main()
