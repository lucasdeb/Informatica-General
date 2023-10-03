import math

def main():
    l = int(input("Ingrese el lado:"))
    r = areacuad(l)/2
    AB = areablanca(l)
    AN = areanegra(l)
    AT = areacuad(l)
    PB = (100*AB)/AT
    PN = (100*AN)/AT
    print("El AN es: {:.2f}".format(AN))
    print("El AB es: {:.2f}".format(AB))
    print("El area TOTAL es: {}".format(AT))
    print("Porc. AB: {:.2f}%  Porc. AN: {:.2f}%".format(PB,PN))
def areacuad(l):
    return (l**2)*2

def areacirc(r):
    return 2*(math.pi*r**2)

def areanegra(l):
    return areacuad(l)+areacirc(l/4)-areacirc(l/2)

def areablanca(l):
    return areacirc(l/2)-areacirc(l/4)
main()
