def main():
    t = int(input("Ingresar tiempo en segundos: "))
    d = t//86400
    h = (t-(86400*d))//3600
    m = (t-((86400*d) + (3600*h)))//60
    s = (t-((86400*d) + (3600*h) + (60*m)))
    
    print("{} Dia(s), {} Hora(s), {} Minuto(s), {} Segundo(s)".format(d,h,m,s))
    
main()