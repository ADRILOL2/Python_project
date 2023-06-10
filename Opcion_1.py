import random
import time

def menu():
    print("""\n       OPCIONES
1. Añadir numero por tu cuenta
2. Añadir numero aleatoriamente
3. Añadir numero entre uno y otro
4. Leer lista
5. Salir
""")
    time.sleep(0.5)
    e=input("Elije una de las opciones:")
    return e

def numero(x):#puedes poner el numero que tu quieras
    return x.append(int(input("pon el numero:")))

def num_aleatorio(x):#permite elejir un numero entre el -100 y el 100
    time.sleep(1)
    n=random.randint(-100,100)
    print("Ha salido un {}\n".format(n))
    return x.append(n)

def numero_entre(x):#elije un numero PERO con la condición que tu pones esos numeros
    a=int(input("Escribe un numero:"))
    b=int(input("Escribe otro numero:"))
    if a>b:
        n=random.randint(b,a)
        print("Entre los numeros {} y {} ha salido un {}\n".format(b,a,n))
        time.sleep(0.5)
        return x.append(n)
    elif a<b:
        n=random.randint(a,b)
        print("Entre los numeros {} y {} ha salido un {}\n".format(a,b,n))
        time.sleep(0.5)
        return x.append(n)
    else:
        print("el unico numero existente es el {}".format(a))
        time.sleep(0.5)
        return x.append(a)

def leer(x):#permite leer la lista de l
    for i,e in enumerate(x):
        print("numero {}: {}".format(i+1,x[i]))

#Programa Principal
def lista_numeros():
    e=0
    l=[]
    while e!=1:
        x=menu()
        match x:
            case "1":
                numero(l)
            case "2":
                num_aleatorio(l)
            case "3":
                numero_entre(l)
            case "4":
                leer(l)
            case "5":   
                print("saliendo. . .")
                time.sleep(1.5)
                e=1
            case other:
                print ("\nERROR\n")
                time.sleep(0.5)
    print("volviendo al menu . . .\n")