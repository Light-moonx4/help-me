#identidad y saludo
def identidad (name,edad):
    print("hola tu es nombre es",name," y tienes",edad,"de edad")

name=(input("digite nombre:"))
edad=int(input("digite edad:"))

identidad(name,edad)