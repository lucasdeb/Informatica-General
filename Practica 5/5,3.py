"""
toma la mitad de la palabra de cantidad de cifras pares
"""

def main():
    pal = str(input("Ingresar palabra con cantidad de cifras pares: "))
    while len(pal)%2!=0:
        pal = str(input("Error. Ingrese una palabra de longitud par: "))
    print(pal[0:len(pal)//2])
main()
                        