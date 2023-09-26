'''
bibliotecas necesarias

pip install nltk 
pip install textblob


'''
#importo las bibliotecas necesarias

import nltk  
from textblob import TextBlob

'''
Descarga recursos de NLTK:
Descarga recursos como un lexicon y un analizador de sentimientos de NLTK:

nltk.download('punkt')
nltk.download('vader_lexicon')

'''

#Utiliza TextBlob para analizar el sentimiento de cada texto. TextBlob utiliza un enfoque basado en reglas 
# y un modelo de análisis de sentimiento para asignar una puntuación de polaridad 
# (positiva, negativa o neutral) a cada texto.

def analizar_sentimiento(texto):
    analysis = TextBlob(texto)
    if analysis.sentiment.polarity > 0:
        return "Positivo"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negativo"
    
# Tus textos para el análisis de sentimiento
tus_textos = [
    "Este es un ejemplo de texto positivo que me hace sentir bien.",
    "No estoy seguro de cómo me siento acerca de esto.",
    "Estoy enojado por la situación actual.",
    "¡Hoy ha sido un día increíblemente mediocre!"
]

# Luego, aplica la función a tus textos
resultados = []
for texto in tus_textos:
    resultado = analizar_sentimiento(texto)
    resultados.append(resultado)

# Imprime los resultados
for i, resultado in enumerate(resultados):
    print(f"Texto {i+1}: {resultado}")