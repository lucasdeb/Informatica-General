def main():
    text = str(input("Ingrese un texto: "))
    pal = str(input("Ingrese una palabra: "))
    if entext(text,pal) == True:
        print("Se cumple con la condicion")
    else:
        print("No se cumple con la condicion")
def entext(text,pal):
    cont = 0
    comp = ""
    true = 0
    false = 0
    while cont != len(text):
        if (("a"<=text[cont]<="z") or ("A"<=text[cont]<="Z")) == True:
            comp += text[cont]
            cont += 1
        else:
            for i in pal:
                if ((("a"<=i<="z") or ("A"<=i<="Z")) == True) and ((i in comp) == True):
                    true += 1
                else:
                    false += 1
            if true == len(pal):
                return True
            else:
                comp = ""
                cont += 1
                true = 0
                false = 0
    for i in pal:
        if ((("a"<=i<="z") or ("A"<=i<="Z")) == True) and ((i in comp) == True):
            true += 1
        else:
            false += 1
    if true == len(pal):
        return True
    else:
        return False
main()
            
        
        