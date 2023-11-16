#Dada una lista de números encontrar el número mayor.
def encontrar_mayor(lista):
    if not lista:  # Verificar si la lista está vacía
        return None

    maximo = lista[0]  # Asignar el primer número como el máximo inicialmente

    for numero in lista:
        if numero > maximo:
            maximo = numero  # Actualizar el número máximo si encontramos uno mayor
    
    return maximo

# Ejemplo de uso:
numeros = [13, 27, 8, 45, 19, 62]
mayor = encontrar_mayor(numeros)
print("El número mayor es:", mayor)
