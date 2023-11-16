#Dada una lista de números hallar la mediana
def encontrar_mediana(lista):
    if not lista:  # Verificar si la lista está vacía
        return None

    # Ordenar la lista de menor a mayor (utilizando el algoritmo de burbuja)
    n = len(lista)
    print (n)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    # Calcular la mediana
    if n % 2 == 0:  # Si la lista tiene un número par de elementos
        mediana = (lista[n // 2 - 1] + lista[n // 2]) / 2
    else:  # Si la lista tiene un número impar de elementos
        mediana = lista[n // 2]
    
    return mediana

# Ejemplo de uso:
numeros = [13, 27, 8, 45, 19, 62]
#8, 13, 19, 27, 45, 62
mediana = encontrar_mediana(numeros)

if mediana is not None:
    print("La mediana de la lista es:", mediana)
else:
    print("La lista está vacía")
