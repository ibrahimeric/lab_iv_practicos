#Importa las bibliotecas necesarias

import os
os.path.abspath("3_unidad\\Actividad 4\\dataset\\validation")
import scipy

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Crear un generador de datos de entrenamiento y validación
train_datagen = ImageDataGenerator(rescale=1.0 / 255)
validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_generator = train_datagen.flow_from_directory(
    os.path.abspath("3_unidad\\Actividad 4\\dataset\\train"),
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary')

validation_generator = validation_datagen.flow_from_directory(
    os.path.abspath("3_unidad\\Actividad 4\\dataset\\validation"),
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary')

# Definir la arquitectura de la CNN
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // 32,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // 32,
    epochs=10)

#Aquí hay un ejemplo de cómo preprocesar una imagen de prueba utilizando TensorFlow:

from tensorflow.keras.preprocessing import image
import numpy as np

# Cargar la imagen de prueba
img_path = '3_unidad/Actividad 4/dataset/test/1.jpg'
img = image.load_img(img_path, target_size=(150, 150))

# Convertir la imagen a un array numpy
img_array = image.img_to_array(img)

# Normalizar los valores de píxeles (escalarlos entre 0 y 1)
img_array = img_array / 255.0

# Expandir las dimensiones para que coincidan con las dimensiones de entrada de la CNN
img_array = np.expand_dims(img_array, axis=0)

'''
Luego, puedes utilizar tu modelo entrenado para realizar la clasificación en la imagen de prueba.
Puedes usar el método predict de tu modelo para obtener la probabilidad de que la imagen sea un perro o un gato.
Aquí hay un ejemplo de cómo hacerlo
'''
# Realizar la clasificación
prediction = model.predict(img_array)

# La predicción es un valor entre 0 y 1; más cercano a 0 significa gato, más cercano a 1 significa perro
if prediction < 0.5:
    print("Es un gato")
else:
    print("Es un perro")

'''
Puedes utilizar bibliotecas como Matplotlib para mostrar la imagen de prueba junto con la clasificación. 
Aquí hay un ejemplo
'''

import matplotlib.pyplot as plt

# Mostrar la imagen
plt.imshow(img)
plt.axis('off')  # Para eliminar los ejes
plt.title("Clasificación: " + ("Perro" if prediction >= 0.5 else "Gato"))
plt.show()
