#Importa las bibliotecas necesarias

import os
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

# Guardar el modelo entrenado en un archivo HDF5
model.save(os.path.abspath("3_unidad\\Actividad 4\\modeloentrenado.keras"))

#En este ejemplo, el script carga una lista de rutas de imágenes en el directorio de prueba y 
# luego recorre cada imagen en el bucle for. Para cada imagen, se realiza la clasificación y se muestra el resultado 
# junto con la ruta de la imagen. Puedes colocar tus imágenes de prueba en el directorio prueba_dir y el script las clasificará una por una.

#Asegúrate de cambiar 'directorio_de_prueba' por la ruta al directorio que contiene 
# tus imágenes de prueba. Con este código, puedes probar varias imágenes sin tener que modificar el script cada vez que desees hacerlo.

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt  # Importa Matplotlib
import os

# Cargar el modelo entrenado
model = load_model(os.path.abspath("3_unidad\\Actividad 4\\modeloentrenado.keras"))

# Directorio que contiene las imágenes de prueba
prueba_dir = (os.path.abspath("3_unidad\\Actividad 4\\dataset\\test"))

# Obtener la lista de archivos de imagen en el directorio de prueba
imagenes_prueba = [os.path.join(prueba_dir, img) for img in os.listdir(prueba_dir)]

# Definir una función para mostrar la imagen y esperar una entrada del usuario
def mostrar_imagen_y_esperar(imagen_path):
    img = image.load_img(imagen_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    plt.imshow(img)
    plt.axis('off')
    plt.title("Clasificación: " + ("Perro" if prediction >= 0.5 else "Gato"))
    plt.show()

    print("Imagen:", imagen_path)
    if prediction >= 0.5:
        print("Clasificación: Perro")
    else:
        print("Clasificación: Gato")

# Mostrar las imágenes una por una y esperar la entrada del usuario
for img_path in imagenes_prueba:
    mostrar_imagen_y_esperar(img_path)
    input("Presiona Enter para mostrar la siguiente imagen...")

# Cerrar todas las ventanas al final
plt.close('all')

    
