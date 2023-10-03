""" SECCIÓN[0] ---------------- T I T U L O ---------------------------------- """
#######################################################  V E R S I O N   #########
###### I N F O R M Á T I C A     G E N E R A L ########  20200427 16:00  #########
##################################################################################

""" SECCIÓN[1]----- D A T O S   E S T U D I A N T E --------- """
""" ------- C O M P L E T A R    O B L I G A T O R I O ------ """
##################################################################################
### FECHA        :  05 / 05 / 2020
### COMISIÓN     :  JT
### EXAMEN Nro   :  3
### EXAMEN [P|R] :  P
### TEMA Nro     :  6
### APELLIDO     :  Debarbieri
### NOMBRE       :  Lucas
### LEGAJO       :  151903205
### DNI          :  42498701
### 
### COMENTARIOS o OBSERVACIONES del estudiante:
### 
###
###
##################################################################################

""" SECCIÓN[2]---- N O M B R E   D E L   A R C H I V O ------ """
##################################################################################
### ¿Como confeccionar el nombre del archivo ?
### [Apellido].IG.[Anio].[Cuatrimestre].[Comisión][NroExamen][TipoExamen][NroTema].py
###
### [Apellido]    -> REEMPLAZAR por tu apellido y nombre, con
###                  la forma apellidoNombre.
###  IG           -> NO se reemplaza, signifa Informática General.
### [Anio]        -> REEMPLAZAR con dos dígitos del año actual. Ej: 20
### [Cuatrimestre]-> REEMPLAZAR con un dígito 1 =  1° Cuatr | 2 = 2° Cuatr.
### [Comisión]    -> REEMPLAZAR por las dos letras de su comisión Ejemplo: BM.
### [NroExamen]   -> REEMPLAZAR por el número (entero) de examen ej: 1.
### [TipoExamen]  -> REEMPLAZAR con P  = Parcial | R = Recuperatorio |
###                  E = Extraordinario.
### [NroTema]     -> REEMPLAZAR por en número(entero) de tema ej: 2.
###  py           -> NO se reemplaza, es la extensión del archivo.
###      
###
### Un ejemplo del "nombre de un archivo" podria ser:
###
###     Ej ->   alvarezMartin.IG.20.1C.BM.1.P.2.py
###
##################################################################################

""" SECCIÓN[3]--- E N V Í O   D E L   A R C H I V O --------- """
##################################################################################
### El archivo .py con la solución deberá ser entregado
### a través de la plataforma EVA UCA
### Dentro de la pagina de la materia en EVA, IR a la
### solapa EVALUACIONES o bien copiar el siguiente link
###
### https://eva.uca.edu.ar/course/view.php?id=1360&section=4
###
### Ahí podrán encontrar una tarea de entrega de parcialito
### Deberán hacer click sobre ella y se abrirá una ventana
### donde aparecerá el botón 'Agregar Entrega'  en el cual deberán hacer click
### sobre él para desplegar una nueva ventana donde podrán realizar la carga del
### archivo
### 
### IMPORTANTE: La tarea será abierta pasados los 15 minutos
### del horario de comienzo de la clase y estará disponible 90 minuto.
### Ejemplo: Si tu clase es de 7:45 a 10:15 => la tarea se
###          abrirá a las 8:00 y se cerrará 9:30
##################################################################################

""" SECCIÓN[4]----- P A R A   E L   P R O F E S O R --------- """
##################################################################################
### COMENTARIOS o OBSERVACIONES del PROFESOR:
### <Reservado para uso del profesor>
###
###
##################################################################################

""" SECCIÓN[5]--- S O L U C I Ó N   A  L A  C O N S I G N A -- """ 
## ↓↓↓↓↓↓↓ ######################################################## ↓↓↓↓↓↓↓↓↓↓ ###
## ↓↓↓↓↓↓↓ ESCRIBA su código de la Solución a partir de AQUI ABAJO  ↓↓↓↓↓↓↓↓↓↓ ###
## ↓↓↓↓↓↓↓ ######################################################## ↓↓↓↓↓↓↓↓↓↓ ###
import random
def main():
    inf=int(input("Ingrese el extremo inferior del intervalo: "))
    sup=int(input("Ingrese el extremo superior del intervalo: "))
    cant=int(input("Ingrese la cantidad de valores de la lista: "))
    lista=cargarLista (inf, sup, cant)
    print ("Lista original")
    imprimirLista(lista)
    num=int(input("\nIngrese el valor a eliminar: "))
    eliminarValor(lista, num)
    print("Lista modificada: ")
    imprimirLista(lista)

def cargarLista(inf,sup,cant):
    cont = 0
    lista = []
    while cont != cant:
        n = random.randrange(inf,sup)
        lista.append(n)
        cont += 1
    return lista

def imprimirLista(lista):
    for i in lista:
        print(i,end="-")
    
def eliminarValor(lista, num):
    while num in lista:
        lista.remove(num)
    return lista
    
main()


