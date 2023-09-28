""" Crea una función en Python que determine si un número 
dado es primo o no. """


def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Comprobar si el número es divisible por cualquier número desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # El número es divisible, por lo que no es primo

    return True  # Si no se encontraron divisores, el número es primo

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número para verificar si es primo: "))

if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")
