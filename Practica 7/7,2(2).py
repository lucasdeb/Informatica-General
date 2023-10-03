def main():
    archivo = open("/Users/lucas/Desktop/7,2.csv","r")
    
    lstlineas = archivo.readlines()
    for linea in lstlineas:
        linea=linea[:-1]
        print(linea)
    print(lstlineas)
    
    archivo.close()
main()