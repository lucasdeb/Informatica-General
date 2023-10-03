def main():
    lsArch = ['central,region,fuente,generacion,anio_mes\n', 'CAPE,COMAHUE,Termica,21868984,2020-01\n', 'AESP,BUENOS AIRES,Termica,193938412,2012-01\n', 'CAPE,COMAHUE,Termica,20009911,2017-03\n', 'ATUC,BUENOS AIRES,Nuclear,269321,2020-03\n', 'AMEGHI,PATAGONICA,Hidraulica,11705,2018-08\n', 'ANAT,NOROESTE,Termica,7670154,2018-07\n','APAR,BUENOS AIRES,Termica,1077474,2015-09\n', 'ARAUEO,NOROESTE,Renovable,844759,2017-02\n', 'ARROHI,COMAHUE,Hidraulica,2961,2012-01\n', 'ATUC,BUENOS AIRES,Nuclear,237003,2019-03\n', 'ULN1FV,CUYO,Renovable,5779081,2020-03\n', 'APAR,BUENOS AIRES,Termica,43969,2020-02\n', 'VLONEO,BUENOS AIRES,Renovable,1171872,2020-02\n']
    n = int(input())
    print("Para n =", n)
    maximo(lsArch, n)
    lsCol=['fuente','region','anio_mes']
    diFiltro={'anio_mes':'2020-03'}
    filtrar(lsArch,lsCol,diFiltro)
    

def maximo(l,n):
    laux=[]
    cont=0
    la=len(l)
    c=[]
    for i in range(len(l)):
        laux.append(l[i][:-1].split(","))

    print("{:15}  {:15}  {:15}".format(laux[0][0],laux[0][3],laux[0][4]))
    laux.pop(0)
    
    while (cont!=n) and (cont!=la-1):
        for x in range(len(laux)):
            if x == 0:
                maxi = laux[x]
            elif int(laux[x][3])>int(maxi[3]):
                maxi = laux[x]
        c.append(maxi)
        laux.remove(maxi)
        cont+=1
        
    if n!=0:
        for x in range(len(c)):
            for y in range(x+1,len(c)):
                if int(c[x][4][0:4])<int(c[y][4][0:4]):
                    temp = c[y]
                    c[y] = c[x]
                    c[x] = temp
                elif (int(c[x][4][0:4]) == int(c[y][4][0:4])) and (int(c[x][4][6:7])<int(c[y][4][6:7])):
                    temp = c[y]
                    c[y] = c[x]
                    c[x] = temp
        for i in c:
            print("{:15}  {:15}  {:15}".format(i[0],i[3],i[4]))
    print('\n')
            
def filtrar(l,lstCol,diFiltro):
    for i in range(len(l)):
        l[i] = l[i][:-1].split(",")
    filtro=-1
    aux=-1
    for i in l[0]:
        aux+=1
        if i in diFiltro.keys():
            filtro=aux
       
    lstFiltrada=[]
        
    if filtro!=-1:
        lstFiltrada.append(l[0])
        for i in l:
            if i[filtro] in diFiltro.values():
                lstFiltrada.append(i)
    elif filtro==-1:
        lstFiltrada+=l
        #lo q tengo q imprimir
    for i in range(len(lstFiltrada)):
        for j in range(len(lstFiltrada[0])):
            if lstFiltrada[0][j] in lstCol:
                print("{:15}".format(lstFiltrada[i][j]),end=" ")
        print('')
        
main()