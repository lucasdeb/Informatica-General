def main():
    ancho = int(input("Ingrese ancho: "))
    alto = int(input("Ingrese alto: "))
    print(crearRectangulo(ancho,alto))
    
def crearFila(ancho):
    
    return "*"*ancho

def crearRectangulo(ancho,alto):
    
    n = crearFila(ancho) + "\n"
    
    return n*alto
main()
    