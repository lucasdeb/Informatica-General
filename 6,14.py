def main():
    d = agregarDicEle2()
    print("El diccionario retornado es: ")
    print(d)
    n = int(input("Ingresar número a traducir o cero para salir: "))
    while n not in d and n != 0:
        n = int(input("Error, ingresa un numero a traducir o 0 para salir: "))
    idioma = str(input("Ingresar idioma [‘en’|’sp’|’de’]: "))
    while (idioma != "en") and (idioma != "sp") and (idioma != "de"):
        idioma = str(input("Error, ingresar idioma [‘en’|’sp’|’de’]: "))
    while n != 0:
        ing = 0
        sp = 1
        de = 2
        if n in d:
            if (idioma == "en"):
                print("{} en ingles: {}".format(n,(d[n][ing])))
            if (idioma == "sp"):
                print("{} en espanol: {}".format(n,(d[n][sp])))
            if (idioma == "de"):
                print("{} en aleman: {}".format(n,(d[n][de])))
        n = int(input("Ingresar número a traducir o cero para salir: "))
        while n not in d and n != 0:
            n = int(input("Error, ingresa un numero a traducir o 0 para salir: "))
        if n != 0:
            idioma = str(input("Ingresar idioma [‘en’|’sp’|’de’]: "))
            while (idioma != "en") and (idioma != "sp") and (idioma != "de"):
                idioma = str(input("Error, ingresar idioma [‘en’|’sp’|’de’]: "))
            
    

def agregarDicEle2():
    d = {}
    salir = "n"
    while salir != "s":
        clave = int(input("Ingresar numero entero: "))
        ing = str(input("Ingresar valor en ingles: "))
        es = str(input("Ingresar valor en espanol: "))
        de = str(input("Ingresar valor en aleman: "))
        valor = (ing,es,de)
        d[clave] = valor
        salir = str(input("Desea salir? (s/n): "))
    return d

main()