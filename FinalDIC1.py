def main():
    lstCiudad = ['223,Parana\n', '114,Merlo\n', '218,Guaymallen\n', '132,C. Rivadavia\n', '341,Adolfo Alsina\n','404,Jose C. Paz\n']
    lstResiduos = ['33,114,200518\n', '31,223,200519\n', '27,218,200319\n', '26,132,200616\n', '74,341,200319\n','62,404,200606\n', '46,218,200709\n', '55,132,200630\n', '55,341,200612\n', '54,404,200701\n','23,114,200315\n', '55,223,200519\n', '34,218,200319\n', '33,132,200425\n', '27,341,200422\n','21,404,200501\n', '31,114,200503\n', '44,114,200513\n', '44,218,200519\n']
    #print(media_01(3,lstCiudad,lstResiduos))
    print(media_02(lstResiduos))

def media_02(lr):
    lr=f1(lr)
    prom=0
    d={}
    cont=0
    # for i in lr:
    #     if int(str(i[2])[2:4]) not in d:
    #         d[int(str(i[2])[2:4])]=0
    #         for elem in lr:
    #             if int(str(i[2])[2:4]) == int(str(elem[2])[2:4]):
    #                 d[int(str(i[2])[2:4])]+=elem[0]
    #                 cont+=1
    #         d[int(str(i[2])[2:4])]/=cont
    #         cont=0

    for i in range(1,12):
        for elem in lr:
            if int(str(elem[2])[2:4]) == i:
                prom+=elem[0]
                cont+=1
        if cont!=0:
            d[i]=prom/cont
            cont=0
            prom=0
    return d


            
    
def media_01(n,lc,lr):
    dc=f(lc)
    lr=f1(lr)
    lf=[]
    d={}
    pt=0
    cont=0
    cont1=0
    
    for cl in dc:
        if cl not in d:
            d[dc[cl]]=0
        for i in lr:
            if cl == i[1]:
                d[dc[cl]]+=i[0]
                pt+=i[0]
                cont+=1
        d[dc[cl]]/=cont
        cont1+=cont
        cont=0
    
    pt = pt/cont1
    maxi=[]
    bandera=True
    while cont!=n:
        for u in d:
           if bandera == True:
               maxi = [u,d[u]]
               bandera = False
           elif d[u]>maxi[1]:
               maxi = [u,d[u]]
        cont+=1
        maxi[1] = "{:.1f}".format(maxi[1])
        lf.append(maxi)
        d.pop(maxi[0])
        bandera=True
        
    return ("{:.2f}".format(pt),lf)
    
def f(l):
    d={}
    l = lstSplit(l)
    for i in l:
        d[int(i[0])]=i[1]
        
    return d

def f1(l):
    l = lstSplit(l)
    for i in l:
        i[0] = int(i[0])
        i[1] = int(i[1])
        i[2] = int(i[2])
    return l

def lstSplit(lst):
    aux=[]
    for elem in lst:
        aux.append(elem[:-1].split(","))
    return aux

main()