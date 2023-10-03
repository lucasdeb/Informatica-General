def main():
    sec = str(input("Ingrese la secuencia de palabras separadas por coma: "))
    print("Palabras:",vocales(sec))
    
def vocales(sec):
    pal = ""
    voc = 0
    cont = 0
    for i in sec:
        if i != ",":
            pal += i
        else:
            for j in range(1,len(pal)):
                if (pal[j-1] != pal[j]) and ((pal[j] == "a") or (pal[j] == "e") or (pal[j] == "i") or (pal[j] == "o") or (pal[j] == "u")) and ((pal[j-1] == "a") or (pal[j-1] == "e") or (pal[j-1] == "i") or (pal[j-1] == "o") or (pal[j-1] == "u")):
                    voc += 2
            if voc>=2:
                cont += 1
                voc = 0
                pal = ""
            else:
                pal = ""
    for j in range(1,len(pal)):
        if (pal[j-1] != pal[j]) and ((pal[j] == "a") or (pal[j] == "e") or (pal[j] == "i") or (pal[j] == "o") or (pal[j] == "u")) and ((pal[j-1] == "a") or (pal[j-1] == "e") or (pal[j-1] == "i") or (pal[j-1] == "o") or (pal[j-1] == "u")):
            voc += 2
        if voc>=2:
            cont += 1
    return cont
main()