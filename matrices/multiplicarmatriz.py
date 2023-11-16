def multiplicar_matrices(matriz1, matriz2):
    if not matriz1 or not matriz2:
        return None  # Devolver None si alguna matriz está vacía

    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    if columnas_matriz1 != filas_matriz2:
        return None  # Devolver None si las dimensiones de las matrices no son adecuadas para la multiplicación

    resultado = []

    for i in range(filas_matriz1):
        fila_resultado = []
        for j in range(columnas_matriz2):
            suma = 0
            for k in range(columnas_matriz1):
                suma += matriz1[i][k] * matriz2[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)

    return resultado

# Ejemplo de uso:
matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_b = [
    [9, 8],
    [6, 5],
    [3, 2]
]

resultado = multiplicar_matrices(matriz_a, matriz_b)
if resultado is not None:
    for fila in resultado:
        print(fila)
else:
    print("Las dimensiones de las matrices no son adecuadas para la multiplicación.")
