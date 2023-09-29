#Importa las bibliotecas necesarias

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense

# Rutas a las carpetas de datos
train_data_dir = '/dataset/train")'  # Ruta a la carpeta de entrenamiento
validation_data_dir = 'dataset/validation'  # Ruta a la carpeta de validación

# Parámetros de preprocesamiento de imágenes
img_width, img_height = 150, 150  # Tamaño de las imágenes
batch_size = 32  # Tamaño del lote (batch size)

# Configuración de aumento de datos para el conjunto de entrenamiento
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,  # Normalización de píxeles
    shear_range=0.2,    # Cambios de inclinación
    zoom_range=0.2,     # Aumento de zoom
    horizontal_flip=True)  # Volteo horizontal aleatorio

# Configuración de aumento de datos para el conjunto de validación (solo normalización)
validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

# Creación de generadores de imágenes para entrenamiento y validación
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')  # 'binary' para clasificación binaria (perros vs. gatos)

validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

# Nota: Los generadores de imágenes cargarán y preprocesarán automáticamente las imágenes

#Crea el modelo de la CNN

model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=(img_width, img_height, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))


#Compila el modelo

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#Entrena el modelo utilizando los generadores de imágenes

model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size)


#Puedes evaluar el modelo en un conjunto de prueba y guardarlo si estás satisfecho con el rendimiento

# Evaluar en un conjunto de prueba (si tienes uno)
test_data_dir = 'dataset/test'

test_datagen = ImageDataGenerator(rescale=1.0 / 255)

test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

score = model.evaluate(test_generator)
print("Loss:", score[0])
print("Accuracy:", score[1])

# Guardar el modelo

model.save("dog_cat_model.h5")
