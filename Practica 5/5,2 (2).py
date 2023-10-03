def main():
    ext = str(input("Ingrese los extremos: "))
    pal = str(input("Ingrese una palabra: "))
    if funcion(ext,pal) == "":
        print("La función ha retornado una palabra vacía")
    else:
        print("La función retornó:",funcion(ext,pal))

def funcion(ext,pal):
    if len(ext)<2:
        return ""
    else:
        return ext[0]+pal+ext[1]
main()