import math
def main():
    lado = int(input("Ingrese la base: "))
    print("La superf. negra es:",areaNegra(lado))
    
def areaNegra(b):
    r = b/2
    area = areaRec(b) - areaCirc(r) - areaTri(b)
    return area
def areaRec(b):
    return b*(2*b)
    
def areaCirc(r):
    return math.pi*(r**2)

def areaTri(b):
    return (b*b)/2

main()