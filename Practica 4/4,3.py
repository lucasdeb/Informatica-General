def main():
    cont = 0
    n = int(input("Ingrese numero: "))
    for i in range(2,n+1):
        if i == 3 or i == 2: 
            print("{}".format(i))
        if i%2 != 0 and i%3!= 0 and i%5!=0:
                print("{}".format(i))
main()