lista_numeros=[8,16,25,27,32,35,55,80,96,102,122]
busqueda=int(input("digite numero a bucar:"))
sw=False
izq=0
der=len(lista_numeros)-1

while sw==False and izq<=der:
    med=(izq + der) //2
    if lista_numeros [med] ==busqueda:
        print("numero encontrado bingo")
        sw=True
    elif lista_numeros [med]>busqueda:
        der=med-1
        print("avanced")
    else:
        izq=med+1
        print("avanced 2")
if not sw:
    print("no encontrado")


