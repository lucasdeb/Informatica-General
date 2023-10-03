def main():
    text = str(input("Ingrese una frase: "))
    if palindroma(text) == True:
        print("La frase es palindroma")
    else:
        print("La frase no es palindroma")
def palindroma(text):
    cont = 0
    text1 = ""
    while cont != len(text):
        if ("a"<=text[cont]<="z") == True:
            text1 += text[cont]
            cont += 1
        elif ("A"<=text[cont]<="Z") == True:
            num = ord(text[cont])
            text1 += chr(num+32)
            cont += 1
        elif text[cont] == " ":
            cont += 1
    if text1 == text1[::-1]:
        return True
    else:
        return False
main()