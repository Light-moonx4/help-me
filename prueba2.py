numeros = [2, 4, 6, 8, 9, 11, 15, 17, 19, 22, 25]
objetivo = int(input("Digite el número que desea encontrar: "))

# El inicio_usuario sigue sin usarse en la lógica principal según tu ajuste anterior
inicio_usuario = int(input(f"Ingresa el índice inicial (0 a {len(numeros)-1}): "))

inicio = 0 
fin = len(numeros) - 1
encontrado = -1

print(f"\nBuscando el {objetivo}...")

# Agregamos 'encontrado == -1' a la condición para detener el ciclo sin usar break
while inicio <= fin and encontrado == -1:
    medio = (inicio + fin) // 2
    print(f"Revisando índice {medio}, valor {numeros[medio]}")

    if numeros[medio] == objetivo:
        encontrado = medio
        # Ya no hay break, el ciclo termina porque 'encontrado' dejó de ser -1
    elif numeros[medio] < objetivo:
        inicio = medio + 1
        print(f"Objetivo mayor, moviendo inicio a {inicio}")
    else:
        fin = medio - 1
        print(f"Objetivo menor, moviendo fin a {fin}")

if encontrado != -1:
    print(f"\n¡Logrado! Elemento encontrado en el índice {encontrado}")
else:
    print("\nElemento no encontrado")
