def main():
    lstAlumnos = ['152002,Juan Gonzalez\n','152001,Ana Martinez\n','151988,Ricardo Bochini\n','180372,Vicente Pernia\n']
    lstMaterias = ['132,Informática Gral\n','127,Álgebra y Geometría\n','137,Física I\n']
    lstCursadas= ['137,152001,4.0\n', '127,151988,6.0\n', '137,151988,7.5\n' ,'132,152002,2.0\n','132,151988,6.0\n', '127,152001,2.0\n', '127,180372,10.0\n']
    print(aprobadas(lstAlumnos,lstMaterias ,lstCursadas,'Ana Martinez'))
    print(segmentos(lstAlumnos,lstMaterias,lstCursadas))
    
    
def segmentos(la,lm,lc):
    d = {"M":[],"R":[],"B":[],"E":[]}
    dA=lst1(la)
    dM=lst2(lm)
    lC=lst3(lc)
    clave = ""
    nombre = ""
    
    for i in lC:
        if i[2]<4:
            d["M"] += [[dM[i[0]],dA[i[1]]]]
        elif 7>i[2]>=4:
            d["R"] += [[dM[i[0]],dA[i[1]]]]
        elif 8>i[2]>=7:
            d["B"] += [[dM[i[0]],dA[i[1]]]]
        else:
            d["E"] += [[dM[i[0]],dA[i[1]]]]
        
    return d

def aprobadas(la,lm,lc,n):
    dA=lst1(la)
    dM=lst2(lm)
    lC=lst3(lc)
    clave = ""
    nombre = ""
    ap = []
    
    for cl in dA:
        if dA.get(cl) == n:
            clave = cl
    
    for i in lC:
        if (i[1] == clave) and (i[2]>=4):
            for nom in dM:
                if nom == i[0]:
                    nombre = dM.get(nom)
            ap.append((nombre,i[2]))
    
    return ap

    
def lst1(l):
    l = lstSplit(l)
    d = {}
    for i in l:
        d[int(i[0])] = i[1]
    return d

def lst2(l):
    l = lstSplit(l)
    d = {}
    for i in l:
        d[int(i[0])] = i[1]
    return d

def lst3(l):
    l = lstSplit(l)
    for i in l:
        i[0] = int(i[0])
        i[1] = int(i[1])
        i[2] = float(i[2])
    return l
    
def lstSplit(lst):
    aux=[]
    for elem in lst:
        aux.append(elem[:-1].split(","))
    return aux

main()
        
        