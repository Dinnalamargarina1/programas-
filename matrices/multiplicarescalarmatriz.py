def multiplicar_por_escalar(matriz, escalar):
    if not matriz:
        return None  # Devolver None si la matriz está vacía

    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            elemento_resultado = matriz[i][j] * escalar
            fila_resultado.append(elemento_resultado)
        resultado.append(fila_resultado)

    return resultado

# Ejemplo de uso:
mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

escalar = 2

resultado = multiplicar_por_escalar(mi_matriz, escalar)
if resultado is not None:
    for fila in resultado:
        print(fila)
else:
    print("La matriz está vacía.")
