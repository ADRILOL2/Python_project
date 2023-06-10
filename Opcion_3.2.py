
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

e=Jugadores()
print(e)