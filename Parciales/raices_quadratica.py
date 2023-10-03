import math 
def main():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    c = int(input("Ingrese c: "))
    
    xpos = (-1*(b) + math.sqrt(b**2 - 4*(a)*(c)))/2*(a)
    
    xneg = (-1*(b) - math.sqrt(b**2 - 4*(a)*(c)))/2*(a)
    
    if a*(xpos)**2 + b*(xpos) + c == 0 and a*(xneg)**2 + b*(xneg) + c == 0:
        print("x = {}".format(xpos))
        print("x = {}".format(xneg))
    else:
        print("No se encontraron raices")
    
    

main()