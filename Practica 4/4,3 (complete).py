def main():
    n = int(input("Input a number: "))
    bet(n)
    al(n)
def bet(n):
    c = 0
    for i in range(1,n+1):
        if i == 2 or i == 3 or i == 5 or (i%2 != 0 and i%3 != 0 and i%5 != 0) and i != 1:
            c += 1 
            if c == 1:
                print("Prime numbers between 1 and {}:".format(n))
                print(i)
            else:
                print(i)
def al(n):
    cont = 0
    num = 1
    while cont <= n:
        if num == 2 or num == 3 or num == 5 or (num%2 != 0 and num%3 != 0 and num%5 != 0) and num != 1:
            if cont == 1:
                print("First {} prime numbers: ".format(num))
                print(num)
            else:
                print(num)
            cont += 1
            num += 1
        else:
            num += 1
main()