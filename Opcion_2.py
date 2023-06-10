def añadir_lista(l):#permite añadir una cosa a la lista
    a=int(input("\nCuantos quieres añadir?\n"))
    while a!=0:
        l.append(input("Escribe:"))
        a-=1

def eliminar_lista(l):#permite eliminar una cosa de la lista
    print(l)
    n=len(l)
    f=int(input("\nCuantos quieres eliminar?\n"))
    while f!=0:
        if f==n:
            print("Eliminando lista completa")
            l.clear()
            f-=n
        elif f<0:
            print("Tomare eso como que no quieres eliminar ninguno.")
            f=0
        elif f>n:
            print("Debe ser igual o menor de {}".format(n))
        elif f==0:
            print("Saliendo. . .")
        else:
            print(l)
            i=int(input("\nCual quieres eliminar?\n"))
            del l[i-1]
            f-=1

def leer_tareas(x):#permite leer la lista de las tareas de casa
    for i,e in enumerate(x):
        print("{}. {}".format(i+1,x[i]))

def menu_tarea():#el meno de la lista que haremos
    print("""
            MENU TAREA
1. Añadir
2. Eliminar
3. Leer
4. Salir
""")
    e=int(input("Elije:"))
    return e

#programa principal
def tarea():
    l=[]
    m="."
    while m!=4:
        m=menu_tarea()
        match m:
            case 1:
                añadir_lista(l)
            case 2:
                eliminar_lista(l)
            case 3:
                leer_tareas(l)
            case 4:
                print("Saliendo. . .")
            case other:
                print("ERROR!")