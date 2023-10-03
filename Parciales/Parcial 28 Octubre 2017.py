def main():
    b = int(input("Ingrese la base: "))
    
    for f in range(0,b):
        for c in range(0,b):
            if (c == 0 or f == 0) or (f == b-1 or c == b-1):
                print("* ",end="")
            else:
                print("  ",end="")
        print()
main()
                
                
