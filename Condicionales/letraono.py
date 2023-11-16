# 7. Escriba un programa para verificar si un caracter es una letra del alfabeto o no.
caracter = input("Ingrese un carácter: ")
if caracter.isalpha():
    print(f"{caracter} es una letra del alfabeto.")
else:
    print(f"{caracter} no es una letra del alfabeto.")
