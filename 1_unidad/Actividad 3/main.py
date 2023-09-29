""" Desarrolla un programa en Python que lea un archivo 
de texto y cuente la cantidad de palabras que contiene. """
import os
def contar_palabras(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            contenido = file.read()
            palabras = contenido.split()  # Dividir el contenido en palabras
            return len(palabras)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró.")
        return 0

# Solicitar al usuario que ingrese el nombre del archivo
nombre_archivo = os.path.abspath(input("Ingresa el nombre del archivo de texto: "))

# Llamar a la función para contar palabras y mostrar el resultado
cantidad_palabras = contar_palabras(nombre_archivo)
print(f"El archivo: \n'{nombre_archivo}'\nContiene: {cantidad_palabras} palabras.")

# CONSOLA. Ruta de acceso al archivo: 1_unidad\\Actividad 3\\archivo_a_contar.txt