b=int(input("da el numero: "))
a=[15, 35, 56,70, 72, 85, 90, 101, 105]
sw=False
izq=0
der=len(a)-1


while sw==False and izq<=der:
    med=(izq + der) //2
    if a [med] ==b:
        print("bingo")
        sw=True
    elif a[med]>b:
        der=med-1
        med=(izq + der) //2
    else:
        izq=med+1
        med=(izq + der) //2
if not sw:
    print("no encontrado")
