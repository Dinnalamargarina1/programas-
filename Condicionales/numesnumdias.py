#Programa para que dado el número del mes, indique el número de días del mes
numero_mes = int(input("Ingrese el número del mes (1-12): "))
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1 <= numero_mes <= 12:
    num_dias = dias_por_mes[numero_mes - 1]
    print(f"El mes {numero_mes} tiene {num_dias} días.")
else:
    print("Número de mes no válido. Debe estar entre 1 y 12.")
