def sumaymult(cantidad):
    numeros = [int(input(f"Introduce el número {i+1}: ")) for i in range(cantidad)]
    multiplicacion = 1
    for numero in numeros:
        suma+=numero
        multiplicacion *= numero
    return suma, multiplicacion

cantidad = int(input("¿Cuántos números quieres ingresar? "))
suma, multiplicacion = sumaymult(cantidad)
print(f"La suma es {suma} y la multiplicación es {multiplicacion}.")