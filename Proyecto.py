import time
import random
import webbrowser
import Opcion_1 as lista_numeros
import Opcion_2 as lista_letras
import Opcion_3 as j
import Opcion_4 as Objetos

def menu_principal():
    print("""           MENU:
1. Lista de numeros
2. Lista
3. Juegos
4. Objetos
5. Salir""")
    e=int(input("Elije:"))
    return e

#Inicio lista de numero
def numero():# permite hacer una lista para poder leero, sumarlo, restarlo...
    lista_numeros.lista_numeros()
# Fin lista de numeros


# Inicio lista de tareas
def lista():#permite hacer listas (por ejemplo de compra, diario y de tareas).
    lista_letras.tarea()
# Final lista de tareas


def juego():#Crear el juego de pulsar rapido
    j.menu_Juego()
#fin de la creación

def objetos():#Animación de cambiar forma a un objeto.
    Objetos.menu_libreria()

f=0
while f!=5:
    f=menu_principal()
    match f:
        case 1:
            numero()
        case 2:
            lista()
        case 3:
            juego()
        case 4:
            objetos()
        case 5:
            print("saliendo. . .")
            time.sleep(1.5)
            print("que tengas un buen dia!")
        case 54357:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        case other:
            print("\n ERROR \n")
            time.sleep(1.5)