from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configura tu clave de API de Google Cloud aquí
API_KEY = 'TU_CLAVE_DE_API'

# Ruta para traducir texto
@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data['text']
    target_lang = data['target_lang']

    # Llamada a la API de Traducción de Google Cloud
    url = f"https://translation.googleapis.com/language/translate/v2?key={API_KEY}"
    payload = {
        'q': text,
        'target': target_lang
    }
    response = requests.post(url, json=payload)
    translation = response.json()['data']['translations'][0]['translatedText']

    return jsonify({'translation': translation})

if __name__ == '__main__':
    app.run(debug=True)
