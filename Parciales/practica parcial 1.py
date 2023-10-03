def main():
    n = str(input("Ingrese numero: "))
    v = n[len(n)-1]
    f = 0
    c = 0
    while c != len(n):
        if n[c] == v:
            c += 1
        else:
            print("No cumple")
            c = len(n)
            f += 1
    if f != 1:
        print("Cumple")
main()