def main():
    n = int(input("Ingrese base: "))
    for f in range(0,n):
        for c in range(0,n):
            if f == c or (f==n//2 and c<=n//2) or (c == n//2 and f<=n//2) or f+c == n-1 or (f+c <= n-1 and f>=n//2) or (f+c <= n-1 and c>= n//2):
                print(" *", end="")
            else:
                print("  ", end="")
        print()
main()
            