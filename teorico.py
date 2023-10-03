def maximo(lsArch,n):
    listaTitulo=cambiarTitulos(lsArch)
    listaDatos=cambiarDatos(lsArch)
    listaFecha=[]
    listaGen=[]
    for subl in listaDatos:
        fecha=subl[4]
        listaFecha.append(fecha)
        gen=subl[3]
        listaGen.append(gen)
    
    ordenarMayAMen(listaFecha)
    ordenarMayAMen(listaGen)
     
    listaN=listaGen[:n]  #Aca tengo la lista con los N datos de generacion, que tengo que ordenar segun fechas. #busco sus fechas y despues las ordeno
    ls=[]
    lst=[]
   
    for sl in listaDatos:
        for elem in listaN:
            if sl[3]==elem:
                central=sl[0]
                generacion=sl[3]
                fecha=sl[4]
                tupla=(central,generacion,fecha)
                ls.append(fecha)
                lst.append(tupla)
                ordenarMayAMen(ls)
    print(listaTitulo)
    for i in ls:
        for j in lst:
            if i==j[2]:
                print(j[0],j[1],j[2])
                
                

def ordenarMayAMen(lst):
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i]<lst[j]:
                aux=lst[i]
                lst[i]=lst[j]
                lst[j]=aux
                
def cambiarTitulos(lsArch):
    listaCompleta=[]
    for linea in lsArch:
        linea=linea[:-1]
        l=linea.split(',')
        listaCompleta.append(l)
    
    listaTitulos=listaCompleta[0]
    return listaTitulos

def cambiarDatos(lsArch):
    listaCompleta=[]
    for linea in lsArch:
        linea=linea[:-1]
        l=linea.split(',')
        listaCompleta.append(l)
        
    listaDatos=listaCompleta[1:]
    for elem in listaDatos:
        elem[3]=int(elem[3])
    return listaDatos
      
def main():
    lsArch=['central,region,fuente,generacion,anio_mes\n','CAPE,COMAHUE,Termica,21868984,2020-01\n','AESP,BUENOS AIRES,Termica,193938412,2012-01\n','CAPE,COMAHUE,Termica,20009911,2017-03\n','ATUC,BUENOS AIRES,Nuclear,269321,2020-03\n','AMEGHI,PATAGONICA,Hidraulica,11705,2018-08\n','ANAT,NOROESTE,Termica,7670154,2018-07\n','APAR,BUENOS AIRES,Termica,1077474,2015-09\n','ARAUEO,NOROESTE,Renovable,844759,2017-02\n','ARROHI,COMAHUE,Hidraulica,2961,2012-01\n','ATUC,BUENOS AIRES,Nuclear,237003,2019-03\n','ULN1FV,CUYO,Renovable,5779081,2020-03\n','APAR,BUENOS AIRES,Termica,43969,2020-02\n','VLONEO,BUENOS AIRES,Renovable,1171872,2020-02\n']
    n=4
    maximo(lsArch,n)
main()
