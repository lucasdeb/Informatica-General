def main():
    pal = input("Ingrese una palabra de longitud par: ")
    cont = 0
    while cont != len(pal):
        if ("a"<=pal[cont]<="z" or "A"<=pal[cont]<="Z") == False:
            pal = input("Error. Ingrese una palabra de longitud par: ")
            cont = 0
        else:
            cont += 1
    
    
    while len(pal)%2 != 0:
        pal = str(input("Error. Ingrese una palabra de longitud par: "))
    print("La funcion ha retornado:",primerMitad(pal))

def primerMitad(pal):
    return pal[0:((len(pal))//2)]
main()