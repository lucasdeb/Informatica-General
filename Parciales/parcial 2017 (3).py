def main():
    cad = str(input("Ingrese cadena de caracteres: "))
    sub = str(input("Ingresar subcadena: "))
    print(repitSub(cad,sub))
    
def repitSub(cad,sub):
    cont = 0
    pos = 0
    pos1 = 0
    string = ""
    comp = ""
    for j in cad:
        if "A"<=j<="Z":
            n = ord(j)
            string += chr(n+32)
        else:
            string += j
    if sub in string:
        while pos1 != len(string):
            if string[pos1] == sub[pos]:
                comp += string[pos1]
                pos1 += 1
                pos += 1
                if comp == sub:
                    cont +=  1
                    comp = ""
                    pos = 0
            else:
                pos1 += 1
    return cont

main()