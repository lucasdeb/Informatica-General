def ordenarLista(lst):
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i][len(lst[i])-4:len(lst[i])]=="cito" and lst[j][len(lst[j])-4:len(lst[j])]=="cion":
                lst[i],lst[j]=lst[j],lst[i]
def main():
    lst=["pancito", "cancion", "locion", "cochecito","multiplicacion"]
    print("Lista original:",lst)
    ordenarLista(lst)
    print("Lista ordenada:",lst)
main()