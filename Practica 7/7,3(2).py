def main():
    archivo = open("/Users/lucasdebarbieri/Downloads/7,3.txt","x")

    print(buscarS(archivo))
    archivo.close()
def buscarS(archivo):
    pal = ""
    comp = ""
    cont = 0
    s = str(input("Ingresar string a buscar: "))
    for i in archivo:
        pal += i
        bandera = False
        v1 = 0
        v2 = 0
    if s in pal:
        for i in range(len(pal)):
            if pal[i] == s[cont]:
                if bandera == False:
                    v1 = i
                    bandera = True
                comp += pal[i]
                cont += 1
                v2 = i
            elif comp == s:
                return (v1,v2)

        
    
        
    
main()
    