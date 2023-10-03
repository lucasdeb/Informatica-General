def main():
    n = int(input("Ingrese la base: "))
    for f in range(0,n+1):
        for c in range(0,n+1):
            if c==n or f==n or f==c or f+c==n or c+f<=n//2:
                print("* ", end="")
            else:
                print("  ",end="")
        print()
main()
        
    