# Suma y multiplicación de 7 números
numeros = [int(input(f"Introduce el número {i+1}: ")) for i in range(7)]
suma = 0
multiplicacion = 1
for numero in numeros:
    suma+=numero
    multiplicacion *= numero

print(f"La suma es {suma} y la multiplicación es {multiplicacion}.")
