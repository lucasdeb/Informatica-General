def main():
    largo = str(input("Ingrese una frase: "))
    corto = str(input("Ingrese una frase: "))
    print("El texto corto se encontro {} veces en el texto largo".format(buscar(largo,corto)))


def buscar(largo,corto):   
    text1 = ""
    cont = 0
    for i in largo:
        if (" " in corto) == True:
            text1 += i
            if corto in text1:
                cont += 1
                text1 = ""
        else:
            if i != " ":
                text1 += i
                if corto in text1:
                    cont+= 1
                    text1 = ""
        
    return cont
main()