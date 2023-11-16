#Dada una lista retorna una nueva lista ordenada de mayor a menor 
def ordenar_mayor_a_menor(lista):
    if not lista:  # Verificar si la lista está vacía
        return []

    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:
                # Intercambiar los elementos si están en el orden equivocado
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

# Ejemplo de uso:
numeros = [13, 27, 8, 45, 19, 62]
lista_ordenada = ordenar_mayor_a_menor(numeros)
print("Lista ordenada de mayor a menor:", lista_ordenada)

