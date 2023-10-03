def main():
    pal = str(input("Ingrese una palabra: "))
    if len(pal) <= 1:
        print("La función ha retornado una palabra vacía")
    else:
        print("La funcion ha retornado:",formar(pal))
    
def formar(pal):
    return (pal[len(pal)-2:len(pal)]*3)


main()