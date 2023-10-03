def main():
    n = int(input("Ingrese la base: "))
    for f in range(0,n):
        for c in range(0,n):
            if f + c <= (n//2)-1 or f == n-1 or c == n-1 or f+c == n-1 or f == c:
                print(" *", end="")
            else:
                print("  ", end="")
        print()
main()