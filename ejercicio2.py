def calcular_potencia(base, exponente):
    return base ** exponente

base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))
resultado = calcular_potencia(base, exponente)
print(f"El resultado de {base}^{exponente} es {resultado}.")
