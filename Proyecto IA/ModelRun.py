import tensorflow as tf
import tensorflow_datasets as tfds
import cv2
import numpy as np

metadatos = tfds.load('fashion_mnist', as_supervised=True, with_info=True)
# Cargar el modelo desde el archivo .h5
modelo = tf.keras.models.load_model('modelo_ropa.h5')

# Leer la imagen en escala de grises
imagen = cv2.imread('playera.jpg', cv2.IMREAD_GRAYSCALE)

# Redimensionar la imagen a 28x28 píxeles
imagen = cv2.resize(imagen, (28, 28))

# Normalizar los valores de los píxeles de la imagen (0-255 a 0-1)
imagen = imagen / 255.0

# Cambiar la forma de la imagen a (28, 28, 1) para que sea compatible con el modelo
imagen = np.expand_dims(imagen, axis=-1)

# Agregar una dimensión extra para representar el lote de tamaño 1, resultando en una forma (1, 28, 28, 1)
imagen = np.expand_dims(imagen, axis=0)


# Realizar la predicción
prediccion = modelo.predict(imagen)

# Imprimir la clase predicha
nombres_clases = metadatos.features['label'].names
clase_predicha = nombres_clases[np.argmax(prediccion)]
print("Predicción: " + clase_predicha)
