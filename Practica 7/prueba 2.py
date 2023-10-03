def main():
    archivo = open("/Users/lucas/Desktop/7,2.csv","r")
    lstDatos = []                         # Lista donde vamos a gurdar los datos del archivo
    
    for linea in archivo:               # recorrer arch  y obtener  cada linea (string)
        linea = int(linea[:-1])               # Eliminar el caracter '\n'(newline), que se encuentra al final del string
        
                                               
        lstDatos.append(linea)

        
    print(lstDatos)
    cont = 0
    total = 0
    for pos in range(0,len(lstDatos)-1):
        for sub in lstDatos[pos]:
            total += int(sub)
            cont += 1
    prom = total/cont
    print(prom)
    archivo.close()                     # cerrar el archivo                                    
main()