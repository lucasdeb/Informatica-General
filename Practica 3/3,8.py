def main():
    n1 = int(input("Ingrese la nota del primer parcial: "))
    n2 = int(input("Ingrese la nota del segundo parcial: "))
    n3 = int(input("Ingrese la nota del tercer parcial: "))
    p = norec(n1,n2,n3)
    if  p>7:
        print("Promociona con promedio de: {}".format(p))
    elif p>4:
        print("El promedio general: {}".format(p))
        print("Alumno debera rendir final")
    
    if n1<4 or n2<4 or n3<4:
        n4 = int(input("Ingrese la nota del recuperatorio: "))
        pr = rec(n1,n2,n3,n4)
        if n4<4:
            print("El alumno fue aplazado")
        else:
            print("Promedio general: {}".format(pr))
            print("El alumno debera rendir final")
    
def norec(n1,n2,n3):
    if n1<4 or n2<4 or n3<4:
        p = (n1+n2+n3)/3
        return p
    
    if n1>3 and n2>3 and n3>3 and ((n1+n2+n3)/3) > 7:
        p = (n1+n2+n3)/3
        return p
    if n1>3 and n2>3 and n3>3 and ((n1+n2+n3)/3) < 7:
        p = (n1+n2+n3)/3
        return p
def rec(n1,n2,n3,n4):
    pr = (n1+n2+n3+n4)/4
    return pr
main()