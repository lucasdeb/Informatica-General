import math

def main():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    c = int(input("Ingrese c: "))
    
    x1 = ((b*(-1)) + math.sqrt((b**2) - 4*a*c))/(2*a)
    x2 = ((b*(-1)) - math.sqrt((b**2) - 4*a*c))/(2*a)
    
    print("Las raices son: {} y {}".format(x1,x2))
    
main()