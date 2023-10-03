def agregarDicEle3():
    dic={}
    z=1
    nota=1
    while z:
        dni=int(input('Ingrese DNI: '))
        nombre=input('Ingrese nombre: ')
        apellido=input('Ingrese apellido: ')
        dic[dni]=[[nombre,apellido],[]]
        nota=int(input('Ingrese las notas, finalice con 0: '))
        while nota!=0:
            dic[dni][1].append(nota)
            nota=int(input())
        z=int(input('¿Desea continuar? (0,1): '))
    return dic

def imprimirDic(dic):
    print("Lista original:",dic)
    
def imprimirDicOrd(dic):
    d={}
    claves = list(dic.keys())
    valores = list(dic.values())
    for i in range(len(claves)-1):
        for y in range(len(claves)-1):
            if claves[y]>claves[y+1]:
                claves[y], claves[y+1] = claves[y+1], claves[y]
                valores[y], valores[y+1] = valores[y+1], valores[y]
    for x in range(len(claves)):
        d[claves[x]]= valores[x]
        
    print("Lista ordenada:",d)
        
        
def main():
    dic=agregarDicEle3()
    imprimirDic(dic)
    imprimirDicOrd(dic)
    
main()