def main():
    vveh = int(input("Velocidad del vehiculo: "))
    vmax = int(input("Velocidad maxima: "))
    em = str(input("Emergencia (s/n): "))
    if em == "s":
        em == True
    elif em == "n":
        em == False
    print(multa(vveh, vmax, em))

def multa(vveh, vmax, em):
    lims = (15*vmax)/100 + vmax
    limi = vmax - (15*vmax)/100
    if em == "s":
        return "No recibe multa"
    while em == "n":
        if vmax/2<vveh<vmax:
            return "No recibe multa"
        if limi<vveh<lims:
            return "Advirtencia"
        if vveh>lims:
            return "Recibe multa por exceso de velocidad"
        if vveh<limi:
            return "Recibe multa por entorpecer el transito"
main()
    
        