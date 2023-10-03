def main():
    lst = cargarLstAlu()
    print("La lista ingresada es: ")
    print(lst)
    print("La lista organizada por dni es: ")
    print(ordenarlstdni(lst))

def cargarLstAlu():
    lst = []
    datos = []
    n = 1
    while n != 0:
        dni = int(input("Ingrese el numero de DNI: "))
        datos.append(dni)
        nombre = str(input("Ingresar el nombre: "))
        datos.append(nombre)
        edad = int(input("Ingresar la edad: "))
        datos.append(edad)
        lst.append(datos)
        datos = []
        n = int(input("Input 0 para terminar: "))
    return lst
        
def ordenarlstdni(lst):
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i][0]<lst[j][0]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst
main()