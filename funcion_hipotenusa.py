#clacular hipotenusa
def hipotenusa (x,y):
    z=((x**2)+(y**2))**(1/2)
    return z

x=float(input("digite el valor del cateto opuesto:"))
y=float(input("digite el valor del cateto adyancente:"))

print("el valor de la hipotenusa es:",hipotenusa(x,y))