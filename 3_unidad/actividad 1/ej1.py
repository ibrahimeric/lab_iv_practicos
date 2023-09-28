import numpy as np

# Datos de ejemplo (reemplaza esto con tus datos reales)
caracteristicas = np.array([1, 2, 3, 4, 5])  # Por ejemplo, número de habitaciones
precios = np.array([100, 150, 200, 250, 300])  # Precios de las casas

# Realizar la regresión lineal simple
a, b = np.polyfit(caracteristicas, precios, 1)

# Imprimir los coeficientes
print(f"Coeficiente a (pendiente): {a}")
print(f"Coeficiente b (intercepto): {b}")

# Función para predecir el precio de una casa en base a las características
def predecir_precio(caracteristica):
    return a * caracteristica + b

# Predecir el precio de una casa con una cierta cantidad de características
caracteristica_nueva = 6  # Cambia esto por el valor que desees predecir
precio_predicho = predecir_precio(caracteristica_nueva)
print(f"Precio predicho para {caracteristica_nueva} características: {precio_predicho}")
