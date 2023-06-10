import time

def cronometro():
    e=3
    while e!=0:
        print("{}...".format(e))
        time.sleep(1)
        e-=1
    print("YA!")
    inicio=time.time()#permite cronometrar el tiempo que pasa al comienzo
    input("")
    fin=time.time()#permite cronometrar el tiempo que ha pasado hasta ahora
    print(round(fin-inicio,2))#round:permite ver los dos digitos atras del numero entero (de 0,2765865896 a 0,27)

cronometro()