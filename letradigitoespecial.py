#Programa para ingresar a cualquier caracter y verificar si es una letra, dígito o carácter especial
caracter = input("Ingrese un carácter: ")
if caracter.isalpha():
    print("Es una letra.")
elif caracter.isdigit():
    print("Es un dígito.")
else:
    print("Es un carácter especial.")