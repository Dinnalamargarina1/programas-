#Escriba un programa para mostrar el patrón como el triángulo de ángulo recto con un asterisco.
#El patrón como:
#*
#**
#***
#****
num_filas = int(input("Ingrese el número de filas para el triángulo: "))
for i in range(1, num_filas + 1):
    print('*' * i)