def main():
    figura()
def figura():
    n = int(input("Ingresa base: "))
    for f in range(0,n+1):
        for c in range(0,n+1):
            if f==c or f+c>n or f>=n//2 or c>=n//2 or f>=n//2 or c>=n//2:
                print(" *",end="")
            else:
                print("  ",end="")
        print()
main()
    