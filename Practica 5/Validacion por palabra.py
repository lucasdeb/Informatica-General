def validar():
    text = str(input("Put some shit: "))
    x = 0
    y = 0
    text1 = ""
    while x != len(text):
        if ("a"<=text[x]<="z") == True:
            x += 1
        else:
            text1 += text[y:x]
            y = x
            x += 1
    print(text1,x,y)
validar()
        