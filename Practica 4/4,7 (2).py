def main():
    des = 0
    apr = 0
    pro = 0
    prom = 0
    n = int(input("Ingrese nota: "))
    while n != 0:
        if 0 < n < 4:
            des += 1
            prom += n
        elif 7 >= n >= 4:
            apr += 1
            prom += n
        elif 10 >= n > 7:
            pro += 1
            prom += n
        n = int(input("Ingrese nota: "))
        total = des+apr+pro
    if total == 0:
        print("\nNo se ingresaron numeros validos...")
    else:
        print("\nCantidad de desaprobados: {} ({:.2f}%)".format(des,(des/total)*100))
        print("Cantidad de aprobados: {} ({:.2f}%)".format(apr,(apr/total)*100))
        print("Cantidad de promocionados: {} ({:.2f}%)".format(pro,(pro/total)*100))    
        print("Promedio General: {}".format(prom/total))
main()
