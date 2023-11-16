#Dada una lista de números retornar el número menor y su posición en la lista
def encontrar_menor(lista):
    if not lista:  # Verificar si la lista está vacía
        return None, None

    menor = lista[0]  # Asignar el primer número como el menor inicialmente
    posicion = 0  # Inicializar la posición del número menor

    
    for i, numero in enumerate(lista):
        if numero < menor:
            menor = numero  # Actualizar el número menor si encontramos uno más pequeño
            posicion = i  # Actualizar la posición del número menor
    
    return menor, posicion

# Ejemplo de uso:
numeros = [13, 27, 8, 45, 19, 62]
menor_numero, posicion = encontrar_menor(numeros)

if menor_numero is not None and posicion is not None:
    print(f"El número menor es {menor_numero} y su posición en la lista es {posicion}")
else:
    print("La lista está vacía")
