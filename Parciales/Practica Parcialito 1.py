import math

def main():
    l = int(input("Ingrese el lado: "))
    r = l/2
    an = areanegra(l)
    ab = areablanca(l)
    at = areacuad(l)
    pb = (100*ab)/at
    pn = (100*an)/at
    print("El AN es: {:.2f}".format(an))
    print("El AB es: {:.2f}".format(ab))
    print("El area TOTAL es: {:.2f}".format(at))
    print("Porc. AB: {:.2f}%  Porc. AN: {:.2f}%".format(pb,pn))

def areacuad(l):
    return 2*(l**2)

def areacirc(r):
    return 2*(math.pi*r**2)

def areanegra(l):
    return areacuad(l)+areacirc(l/4)-areacirc(l/2)

def areablanca(l):
    return areacirc(l/2)-areacirc(l/4)

main()