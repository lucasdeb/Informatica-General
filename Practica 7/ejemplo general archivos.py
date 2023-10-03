#---------------------------------------------------------------#
# CASO 1: 
def leerArch1():    
#'''
#  Función que lee un archivo con readlines.
#  Imprime la lista resultante de la lectura con readlines
#'''
    print("----------leerArch1()---------------")
    
    print("-Con readlines, imprime lista ------")
    arch = open("/Users/lucas/Downloads/archLec.txt","r")      # Abrir archivo de lectura
    lstLinea = arch.readlines()         # leer todas las lineas del archivo y guardar en una lista lstLinea
    print(lstLinea)                     # imprimir la lista con el contenido de las lineas del archivo
                                        # se ven (en la salida) los caracteres newline '\n' en el string
                                        # que contiene cada elemento de la lista
    arch.close()                        # cerrar el archivo
                                    
#---------------------------------------------------------------#
# CASO 2
def leerArch2():
#    '''
#    Función que lee un archivo con readlines 
#    Imprime iterando con un ciclo la lista resultante de la lectura con readlines
#    '''
    print("----------leerArch2()---------------")
    print("-Con readlines, recorre lista ------")
    arch = open("/Users/lucas/Downloads/archLec.txt","r")      # Abrir archivo de lectura
    lstLinea = arch.readlines()         # leer todas las lineas del archivo y guardar en una lista
    for linea in lstLinea:              # recorrer lstLinea (list) y obtengo cada linea (string)
       linea=linea[:-1]                 # Eliminar el caracter '\n'(newline), que es el último caracter del string linea
       print(linea)                     # imprimir la linea
    arch.close()                        # cerrar el archivo
                                    
#---------------------------------------------------------------#
# CASO 3
def leerArch3():
#   '''
#   Función ee un archivo con readline
#   imprime el string de la línea que retorna readline, 
#   Itera haciendo lectura de cada linea hasta el fin del archivo
#   '''
    print("----------leerArch3()---------------")
    print("-Con readline, imprime string - -----")
    arch = open("/Users/lucas/Downloads/archLec.txt","r")      # Abrir archivo de lectura
    linea=arch.readline()               # leer una linea del archivo (antes de entrar al ciclo). Escribe el contenido en linea (Srting)
    while linea!="":                    # mientras haya una linea en el archivo (linea=="", entonces es le fin del archivo)      
        linea = linea[:-1]              # Eliminar el caracter '\n'(newline), que es el último del string linea
        print(linea)                    # imprimir la linea la cual contiene la informaciin de la ´linea leída del archivo.
        linea=arch.readline()           # leer una linea del archivo (dentro del ciclo)
    arch.close()                        # cerrar el archivo
#---------------------------------------------------------------#
# CASO 4
def leerArch4():
    print("----------leerArch4()---------------")
    print("-iterando io.TextIOWrapper (objeto iterable del archivo de texto)------")
    arch = open("/Users/lucas/Downloads/archLec.txt","r")       # Abrir archivo "miArch.txt" de lectura "r". arch contien
                                        # arch es un objeto de clase _io.TextIOWrapper (es el iterable del archivo de texto abierto !!)
    for linea in arch:                  # al iterar arch se obtiene (en cada iteración) la linea "string" que está determinado por el '\n' al final   
        print(linea[:-1])               # imprimir linea. El [:-1] esta para no imprimir el último caracter de la linea (que es donde está el '\n'
    arch.close()                        # cerrar el archivo    
#---------------------------------------------------------------#
# CASO 5
def leerArch5():
    print("----------leerArch5()---------------")
    print("-iterando el archivo ....------")
    print("-Luego se hace un split (se divide el string por sus <<comas>>)  ....------")
    print(" --Creando una lista de sublista (con los elementos del archivo)")

    arch = open("/Users/lucas/Downloads/archLec.txt","r")       # Abrir archivo de lectura
    lstDatos=[]                         # Lista donde vamos a gurdar los datos del archivo
    
    for linea in arch:                  # recorrer arch  y obtener  cada linea (string)
        linea= linea[:-1]               # Eliminar el caracter '\n'(newline), que se encuentra al final del string
        lstLinea=linea.split(",")       # partir el string en listas determinadas por la <<coma>> dentro del string
                                        # << convertir los datos a su formato original
        lstLinea[0]=int(lstLinea[0])    # << de str a int
        lstLinea[1]=int(lstLinea[1])    # << de str a int 
        lstLinea[2]=float(lstLinea[2])  # << de str a float
        lstLinea[4]=int(lstLinea[4])    # << de str a int
        
        lstDatos.append(lstLinea)       # agregar la linea (en formato de lista) a la lista lstDatos 
              
    imprimirLista(lstDatos)             # imprimir la lista de lista lstDatos
    arch.close()                        # cerrar el archivo                                    

def imprimirLista(lst):
     for linea in lst:
        print("{:3d}{:4d} {:>8.3f}  {:20}{:4}".format(linea[0],linea[1],linea[2],linea[3],linea[4]))
#---------------------------------------------------------------#
# CASO 6

def escribirArch():
    print("----------escribirArch()---------------")
    import random
    arch = open("archEsc.txt","w")      # Abrir archivo "archEsc.txt" de escritura
    
    a=random.randint(0,99)              # cargo números aleatorios
    b=random.randint(0,99)
    c=random.randint(0,99)
    
    contenido = "23,5,9\n34,78,9\n"     # escribir un string con el contenido 
    contenido += str(a)+","+str(b)+","+str(c)+"\n"
    
    arch.write(contenido)               # escribir archivo
    arch.write("0,0,0\n")               # escribir archivo
    arch.close()                        # cerrar el archivo     
    print("----se escribió el archivo archEsc.txt--")
#---------------------------------------------------------------#
# CASO 7

def escribirAppendArch():
    print("----------escribirAppendArch()---------------")
    import random
    arch = open("archApp.txt","a")      # Abrir archivo "archApp.txt" de append (agregar o  anexar)
    
    a=random.randint(0,99)              # cargo números aleatorios
    b=random.randint(0,99)
    c=random.randint(0,99)    
                                        # escribir un string con el contenido 
    contenido  = str(a)+","+str(b)+","+str(c)+"\n"
    
    arch.write(contenido)               # escribir archivo

    arch.close()                        # cerrar el archivo     
    print("----agregó en el archivo archApp.txt--")
  

  
def main():

    leerArch1()
    leerArch2()
    leerArch3()
    leerArch4()
    leerArch5()
    escribirArch()
    escribirAppendArch()

main()