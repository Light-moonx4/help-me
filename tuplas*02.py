matriz=[]
n=int(input("digite el tamaño filas :"))
m=int(input("digite el tamaño de las columnas:"))

for i in range (0,n,1):
    for j in range(0,m,1):
        matriz = input(f"Digite la letra para la posición [{i}][{j}]: ")

for i in range (0,n,1):
    for j in range (0,m,1):
        print(matriz[i][j])
    print("\n")

