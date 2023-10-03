def main():
    text = str(input("Ingrese un texto: "))
    if principioFin(text) == True:
        print("El texto cumple con la condicion")
    else:
        print("El texto no cumple con la funcion")
        
def principioFin(text):
    primer = ""
    text1 = ""
    rev = text[::-1]
    prim = 0
    cont = 0
    while prim == 0:
        if ("a"<=text[cont]<="z") == True:
            primer += text[cont]
            cont += 1
        elif ("A"<=text[cont]<="Z") == True:
            num = ord(text[cont])
            primer += chr(num+32)
            cont += 1
        else:
            prim += 1
    cont = 0
    while rev[cont] != " ":
        if ("a"<=rev[cont]<="z") == True:
            text1 += rev[cont]
            cont += 1
        elif ("A"<=rev[cont]<="Z") == True:
            num = ord(rev[cont])
            text1 += chr(num+32)
            cont += 1
        else:
            cont += 1
    final = text1[::-1]
    if primer == final:
        return True
    else:
        return False
            

main()
                
                
    