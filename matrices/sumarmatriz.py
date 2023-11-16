def sumar_matrices(matriz1, matriz2):
    if not matriz1 or not matriz2:
        return None  # Devolver None si alguna matriz está vacía
    
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return None  # Devolver None si las matrices no tienen las mismas dimensiones
    
    filas = len(matriz1)
    columnas = len(matriz1[0])
    suma = []

    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            suma_elemento = matriz1[i][j] + matriz2[i][j]
            fila_suma.append(suma_elemento)
        suma.append(fila_suma)

    return suma

# Ejemplo de uso:
matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = sumar_matrices(matriz_a, matriz_b)
if resultado is not None:
    for fila in resultado:
        print(fila)
else:
    print("Las matrices no tienen las mismas dimensiones y no se pueden sumar.")
