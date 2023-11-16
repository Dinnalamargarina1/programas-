#2. Programa para hallar el mayor de 3 números reales
A=int(input("digite un número "))
B=int(input("digite un número "))
C=int(input("digite un número "))
if A>B:
    if A>C:
        print("El mayor es", A)
    else:
        print("El mayor es", C)
else:
    if C>B:
        print("El mayor es", C)
    else:
        print("El mayor es", B)
print("Fin")
