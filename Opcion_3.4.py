import time
import random

def funcion(e):#ordena el tiempo de forma que el numero mas pequeño sea el primero en la lista
    return e[1]

def tiempo():
    inicio=time.time()#permite cronometrar el tiempo que pasa al comienzo
    input("")
    fin=time.time()#permite cronometrar el tiempo que ha pasado hasta ahora
    e=round(fin-inicio,3)
    print(e)#round:permite ver los dos digitos atras del numero entero (de 0,2765865896 a 0,27)
    return e

def cronometro():#Comienza el juego de quien de los jugadores tiene mas agilidad
    e=3
    print("listo...")
    time.sleep(random.randint(1,5))#elije un numero aleatorio del 1 al 5 cual se vuelven segundos
    print("YA!")
    r=tiempo()
    if r==0:# Al momento de pulsar antes del tiempo debido, tienes que volver a empezar
        reset=0
        print("\nHas pulsado antes de tiempo, vuelve a intentar")
        while reset!="":
            reset=input("")
            cronometro()
    else: #si es un numero distinto al 0, puede añadirse a la lista
        return r

def Jugadores():#Se decidira cuantos jugadores van a jugar con un minimo de 2 y maximo de 6
    lista_jugadores=[]
    i=1
    while i>-1:
        n=int(input("Cuantos jugadores vais a ser?\n"))
        if n==1:
            print("No vas a jugar solo si estas en multijugador, es logica-\n")
            Jugadores()
        elif n<1:
            print("Hay que ser idiota como para que tu elijas que no va a jugar nadie XDDD\n")
            Jugadores()
        while i<n+1:
            e=input("Nombre de jugador {}:".format(i))
            lista_jugadores.append(e)
            i+=1
        i=-1
    return lista_jugadores

def multijugador():
    a=Jugadores()#lista de jugadores
    lista_tiempo=[] #lista del tiempo que dura cada jugador en aprear el boton.
    for i,e in enumerate(a):#se decide en orden de lista de jugadores (del 1º al ultimo)
        s="e"
        while s!="":
            s=input("\n\n{}, es tu turno\n".format(a[i]))
        c=cronometro()
        lista_tiempo.append([a[i],c])
    lista_tiempo.sort(key=funcion)
    for i,e in enumerate(lista_tiempo):
        print ("{}º.{}".format(i+1,lista_tiempo[i]))

multijugador()