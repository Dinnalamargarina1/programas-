#Dada una lista de números hallar la media 
def calcular_media(lista):
    if not lista:  # Verificar si la lista está vacía
        return None
    
    suma = 0
    cantidad = 0

    for numero in lista:
        suma += numero  # Sumar cada número a la suma total
        cantidad += 1   # Contar la cantidad de números
    
    media = suma / cantidad  # Calcular la media dividiendo la suma entre la cantidad de números
    return media

# Ejemplo de uso:
numeros = [13, 27, 8, 45, 19, 62]
media = calcular_media(numeros)

if media is not None:
    print("La media de la lista es:", media)
else:
    print("La lista está vacía")
