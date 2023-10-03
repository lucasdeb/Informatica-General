def main():
    n = float(input("Ingrese un numero con decimal: "))
    
    f = n%1
    
    e = n//1
    
    print("La parte entera es: {}".format(e))
    print("La parte fraccionaria es: {}".format(f))
    
main()
    