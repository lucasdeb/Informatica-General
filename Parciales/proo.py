def main():
    ancho = int(input("Ingrese ancho: "))
    alto = int(input("Ingrese alto: "))
    a=crearfila(ancho)
    b=crearrectangulo(a,alto)
    print(b)
    
    
def crearfila(ancho):
    a= "*"* ancho
    
    return a

def crearrectangulo(a,alto):
    b=(a + "\n")*alto
    return b
    
    
    
main()