# Desarrolla un chatbot en Python que proporcione información sobre el 
# clima actual utilizando una API de pronóstico del tiempo.

# Un ejemplo seria ingresar "us.90001" para obtener la temperatura 
# actual en Los Angeles, California, Estados Unidos.

import requests

# Reemplaza 'TU_API_KEY' con tu clave API real de Weather Unlocked
api_key = '15da9a1bc251d76e7e45650860844bc4'

def obtener_clima_pais(pais_codigo):
    base_url = f"http://api.weatherunlocked.com/api/current/{pais_codigo}?app_id=c1d682f6&app_key=15da9a1bc251d76e7e45650860844bc4"
    

    try:
        response = requests.get(base_url)
        data = response.json()

        if 'wx_desc' in data:
            clima_descripcion = data['wx_desc']
            temperatura_celsius = data['temp_c']
            mensaje = f"La temperatura actual en la ubicacion especificada es de {temperatura_celsius}°C."
        else:
            mensaje = f"No se pudo obtener información para {pais_codigo}."
    except Exception as e:
        mensaje = f"Hubo un error al obtener el clima: {str(e)}"

    return mensaje

while True:
    pais_codigo = input("Por favor, ingresa el código de ubicación del país (o 'salir' para salir): ")
    
    if pais_codigo.lower() == 'salir':
        break
    
    resultado = obtener_clima_pais(pais_codigo)
    print(resultado)