def main():
    n1 = int(input("Ingrese primer numero:"))
    n2 = int(input("Ingrese segundo numero:"))
    n3 = int(input("Ingrese tercer numero:"))
    n = sortear(n1, n2, n3)
    print(n)
def sortear(n1,n2,n3):
    if n1 > n2 > n3:
        n = n3, n2, n1
    if n3 > n2 > n1:
        n = n1, n2, n3
    if n2 > n3 > n1:
        n = n1, n3, n2
    if n2 > n1 > n3:
        n = n3, n1, n2
    if n1 > n3 > n2:
        n = n2, n3, n1
    if n3 > n1 > n2:
        n = n2, n1, n3
    return n 
main()