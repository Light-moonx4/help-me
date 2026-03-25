n = int(input("Digite el número de filas: "))
m = int(input("Digite el número de columnas: "))

matriz = []

for i in range(n):
    fila = []
    for j in range(m):
        letra = input(f"Digite la letra para la posición [{i}][{j}]: ")
        fila.append(letra)
    matriz.append(fila)

print("\nTu matriz es:")
for fila in matriz:
    print(fila)
