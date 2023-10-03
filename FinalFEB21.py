def main():
    lstEnergia = ['101205, 1, 24.2\n', '110607, 8, 54.4\n', '120318, 3, 58.1\n', '090501, 9, 88.4\n', '101209, 1, 26.8\n', '101217, 3, 22.4\n', '190101, 8, 44.0\n']
    lstParque = ['1,Rosario, 8\n', '6,San Martin, 4\n', '8,Lavalle, 10\n', '3,Esperanza, 3\n', '7,General Pico, 9\n', '9,P.Madryn, 4\n']
    print(minimos(lstEnergia))
    print(energiaTotal(3, lstEnergia, lstParque))
    
def minimos(l):
    bandera = True
    AA = ""
    AAMM = ""
    cEnergiaA=0
    cEnergiaM=0
    for i in l:
        lst = i.split(",")
        lst[1] = int(lst[1])
        lst[2] = float(lst[2][:-1])
        if bandera == True:
            cEnergiaA = lst[2]
            bandera = False
        else:
            if lst[2]<cEnergiaA:
                cEnergiaA = lst[2]
                cEnergiaM = lst[2]
                AA = lst[0][0:2]
                AAMM = lst[0][0:4]
    return [(AA,cEnergiaA),(AAMM,cEnergiaM)]

def energiaTotal(n, lstEnergia, lstParque):
    le=[]
    lp=[]
    aux=[]
    cont=0
    for i in lstEnergia:
        aux = i.split(",")
        aux[1] = int(aux[1])
        aux[2] = float(aux[2][:-1])
        le.append(aux)
    for y in lstParque:
        aux = y.split(",")
        aux[0] = int(aux[0])
        aux[2] = int(aux[2][:-1])
        lp.append(aux)
        
    aux=[]
    d={}
    for pid in le:
        if pid[1] not in d:
            d[pid[1]] = pid[2]
        else:
            d[pid[1]] += pid[2]

    bandera = True
    while cont!=n:
        for i in d:
            if bandera == True:
                maxi=i
                bandera = False
            elif d[i]>d[maxi]:
                maxi=i
        CEP = d[maxi]
        for nom in lp:
            if nom[0] == maxi:
                nombre_parque = nom[1]
                CEM = CEP/nom[2]
        aux.append([nombre_parque,CEP,CEM])
        d.pop(maxi)
        cont+=1
        bandera = True
        
        
    return aux
            
    
main()
    