def main():
    generarT1()

def generarT1():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    cont = 0
    rest = 0
    if a > b:
        while cont != 3:
            while (rest + cont)-1!= a-b:
                for i in range(b,a+1):
                    if i%2!=0 and a%i==0:
                        cont+=1
                        print("[{}]: {}".format(cont,i))
                    else:
                        rest += 1
    else:
         while cont != 3:
             while (rest + cont)-1 != b-a:
                for i in range(a,b+1):
                    if i%2!=0 and b%i==0:
                        cont+=1
                        print("[{}]: {}".format(cont,i))
                else:
                    rest += 1
main()