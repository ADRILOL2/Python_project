import time
class Formas:
    def __init__(self, Area, Perimetro):
        self.Area=Area
        self.Perimetro=Perimetro

    def Area(self):
        pass

    def Perimetro(self):
        pass

class cuadrado(Formas):
    def __init__(self, base):
        self.base=base

    def Area(self):
        return self.base * self.base
    
    def Perimetro(self):
        return self.base + self.base

class circulo(Formas):
    def __init__(self, radio):
        self.radio=radio

    def Area(self):
        area=3.14*self.radio**2
        return area
    
    def Perimetro(self):
        perimetro=3.14*self.radio*2
        return perimetro

class triangulo(Formas):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base=base
        self.altura=altura
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3

    def Area(self):
        area=(self.base*self.altura)/2
        return area
    
    def Perimetro(self):
        perimetro=self.lado1+self.lado2+self.lado3
        return perimetro

class rombo(Formas):
    def __init__(self, diagonal_menor, diagonal_mayor):
        self.diagonal_menor=diagonal_menor
        self.diagonal_mayor=diagonal_mayor

    def Area(self):
        area=(self.diagonal_mayor*self.diagonal_menor)/2
        return area
    
    def Perimetro(self):
        perimetro=*4(self.diagonal_mayor**2+self.diagonal_menor**2)**0,5
        return perimetro
    
class rectangulo(cuadrado,Formas):
    def __init__(self, base, altura):
        super().__init__(base)
        self.altura=altura

    def Area(self):
        area=self.base*self.altura
        return area
    
    def Perimetro(self):
        perimetro=self.base+self.altura
        return perimetro

def info_cuadrado(lista):
    n=cuadrado(base=int(input("Que longitud de base le pondras?\n")))
    lista.append(n)

def info_circulo(lista):
    n=circulo(radio=int(input("Que longitud del radio (del centro al lateral del circulo) le quieres poner?\n")))
    lista.append(n)

def info_triangulo(lista):
    b=int(input("Longitud de base:"))
    a=int(input("Altitud:"))
    l1=int(input("Longitud Lado 1:"))
    l2=int(input("Longitud Lado 2:"))
    l3=int(input("Longitud Lado 3:"))
    n=triangulo(b,a,l1,l2,l3)
    lista.append(n)

def info_rectangulo(lista):
    dm=int(input("Escribe un numero:"))
    dM=int(input("Escribe un numero mayor a {}:".format(dm)))
    n=rectangulo(dM,dm)
    lista.append(n)

def menu_libreria():
    lista=[]
    menu=""
    while menu!=7:
        print("""         Calculadora de areas y peirmetros
1.Cuadrado
2.Circulo
3.Triangulo
4.Rectangulo
5.Leer
6.Calcular
7.Salir
""")
        menu=int(input("Cual elijes?\n"))
        match menu:
            case 1:
                info_cuadrado(lista)
            case 2:
                info_circulo(lista)
            case 3:
                info_triangulo(lista)
            case 4:
                info_rectangulo(lista)
            case 5:
                for i,e in enumerate(lista):
                    print(lista[i])
            case 6:
                print("{:5} {:5} {:5}".format("Forma"," Area"," Perimetro"))
                for e in lista:
                    if type(e)==cuadrado:
                        area=e.Area()
                        perimetro=e.Perimetro()
                        print("Cuadrado {:5} {:5}".format(area,perimetro))
                    elif type(e)==circulo:
                        area=e.Area()
                        perimetro=e.Perimetro()
                        print("Circulo {:5} {:5}".format(area,perimetro))
                    elif type(e)==triangulo:
                        area=e.Area()
                        perimetro=e.Perimetro()
                        print("Triangulo {:5} {:5}".format(area,perimetro))
                    elif type(e)==rectangulo:
                        area=e.Area()
                        perimetro=e.Perimetro()
                        print("Rectangulo {:5} {:5}".format(area,perimetro))
            case 7:
                print("Saliendo. . .")
                time.sleep(1.5)
            case other:
                print("Error, Vuelve a intentarlo")
