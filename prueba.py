numeros = [2, 4, 6, 8, 9, 11, 15, 17, 19, 22, 25]
objetivo = int(input("Digite el número que desea encontrar: "))

# El usuario elige un punto de partida sugerido
punto_partida = int(input(f"Ingresa el índice donde quieres empezar a mirar (0 a {len(numeros)-1}): "))

# IMPORTANTE: Para poder "retroceder", el rango siempre debe ser TODA la lista
inicio = 0 
fin = len(numeros) - 1
encontrado = -1

print(f"\nBuscando el {objetivo} en toda la lista (referencia inicial: índice {punto_partida})...")

# Usamos el punto de partida como el primer 'medio' si es válido
primer_intento = True

while inicio <= fin and encontrado == -1:
    if primer_intento:
        medio = punto_partida
        primer_intento = False
    else:
        medio = (inicio + fin) // 2
    
    valor_medio = numeros[medio]
    print(f"Revisando índice {medio}, valor {valor_medio}")

    if valor_medio == objetivo:
        encontrado = medio
    elif valor_medio < objetivo:
        inicio = medio + 1
        print(f"  Objetivo mayor, buscando hacia adelante (Nuevo inicio: {inicio})")
    else:
        fin = medio - 1
        print(f"  Objetivo menor, 'retrocediendo' búsqueda (Nuevo fin: {fin})")

if encontrado != -1:
    print(f"\n¡Logrado! Encontrado en el índice {encontrado}")
else:
    print("\nElemento no encontrado en ninguna parte de la lista.")
