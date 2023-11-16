#Escriba una función que indique las dimesiones de una matriz 
def dimensiones_matriz(matriz):
    if not matriz or not isinstance(matriz, list) or not isinstance(matriz[0], list):
        return 0, 0  # Devolver 0 para filas y columnas si la matriz está vacía o no es válida
    
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    
    return filas, columnas

# Ejemplo de uso:
mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

num_filas, num_columnas = dimensiones_matriz(mi_matriz)
print(f"La matriz tiene {num_filas} filas y {num_columnas} columnas.")
