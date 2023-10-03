"""
Invertir la palabra (de cantidad de cifras pares)
"""



def main():
    pal = str(input("Ingresar palabra: "))
    while len(pal)%2!=0:
        pal = str(input("Error. Ingresar palabra: "))
    p2 = pal[len(pal)//2:len(pal)]
    p1 = pal[0:len(pal)//2]
    print(p2+p1)
main()