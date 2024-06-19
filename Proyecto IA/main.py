### Mauricio Becerra Guzman - 21310105 ###
import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import math
import numpy as np
import cv2

datos, metadatos = tfds.load('fashion_mnist', as_supervised=True, with_info=True)
#print(metadatos)
datos_entrenamiento, datos_pruebas = datos['train'], datos['test']
nombres_clases = metadatos.features['label'].names
print(nombres_clases)

#Funcion de normalizacion para los datos (Pasar de 0-255 a 0-1)
#Hace que la red aprenda mejor y mas rapido
def normalizar(imagenes, etiquetas):
    imagenes = tf.cast(imagenes, tf.float32)
    imagenes /= 255 #Aqui lo pasa de 0-255 a 0-1
    return imagenes, etiquetas

#Normalizar los datos de entrenamiento y pruebas con la funcion que hicimos
datos_entrenamiento = datos_entrenamiento.map(normalizar)
datos_pruebas = datos_pruebas.map(normalizar)

#Agregar a cache (usar memoria en lugar de disco, entrenamiento mas rapido)
datos_entrenamiento = datos_entrenamiento.cache()
datos_pruebas = datos_pruebas.cache()

#Mostrar una imagen de los datos de pruebas, de momento mostremos la primera
for imagen, etiqueta in datos_entrenamiento.take(1):
    break
imagen = imagen.numpy().reshape((28,28)) #Redimensionar, cosas de tensores, lo veremos despues

#######################################################################
#Imprimir imagenes con categoria ejemplo
plt.figure()
plt.imshow(imagen, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
# plt.show()

#Dibujar mas
plt.figure(figsize=(10,10))
for i, (imagen, etiqueta) in enumerate(datos_entrenamiento.take(25)):
    imagen = imagen.numpy().reshape((28,28))
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(imagen, cmap=plt.cm.binary)
    plt.xlabel(nombres_clases[etiqueta])
# plt.show()
########################################################

#Crear el modelo
modelo = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), input_shape=(28,28,1), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2), #2,2 es el tamano de la matriz

    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2), #2,2 es el tamano de la matriz

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=100, activation='relu'),
    tf.keras.layers.Dense(units=50, activation='relu'),
    tf.keras.layers.Dense(units=60, activation='relu'),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax) #Capa de salida con 10 neuranas Para redes de clasificacion con activacion softmax para asegurar que las sumas siempre nops den 1

])

#Compilar el modelo
modelo.compile(
    optimizer='adam', #Utilizamos adam como modelo de optimizacion porque asi aprende y usa retroalimentacion
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),#funcion de perdida
    metrics=['accuracy']
)

#Los numeros de datos en entrenamiento y pruebas (60k y 10k)
num_ej_entrenamiento = metadatos.splits["train"].num_examples
num_ej_pruebas = metadatos.splits["test"].num_examples

print(num_ej_entrenamiento)
print(num_ej_pruebas)

#Usamos lotes ya que el trabajo por lotes permite que entrenamientos con gran cantidad de datos se haga de manera mas eficiente
TAMANO_LOTE = 32

#Shuffle y repeat hacen que los datos esten mezclados de manera aleatoria para que la red no se vaya a aprender el orden de las cosas
datos_entrenamiento = datos_entrenamiento.shuffle(num_ej_entrenamiento).batch(TAMANO_LOTE).repeat()#En shuffle indicamos la cantidad de ejemplos de entrenamientom, bath el tamaño de lote de entrenamiento
datos_pruebas = datos_pruebas.batch(TAMANO_LOTE)

#Entrenamos el la red neuronal
historial = modelo.fit(datos_entrenamiento, epochs=60, steps_per_epoch= math.ceil(num_ej_entrenamiento/TAMANO_LOTE))

#Ver la funcion de perdida en cada epoca
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])
plt.show()

#######################################################################################################
# Pintar una cuadricula con varias predicciones, y marcar si fue correcta (azul) o incorrecta (roja)  #
#######################################################################################################

# Itera sobre cada lote de imágenes de prueba y etiquetas en el conjunto de datos de pruebas.
for imagenes_prueba, etiquetas_prueba in datos_pruebas.take(1):
  # Convierte las imágenes de prueba y las etiquetas a arreglos numpy para su procesamiento.
  imagenes_prueba = imagenes_prueba.numpy()
  etiquetas_prueba = etiquetas_prueba.numpy()
  # Utiliza el modelo para predecir las etiquetas de las imágenes de prueba.
  predicciones = modelo.predict(imagenes_prueba)

# Define una función para graficar la imagen junto con su predicción y etiqueta real.
def graficar_imagen(i, arr_predicciones, etiquetas_reales, imagenes):
    # Extrae la predicción, la etiqueta real y la imagen correspondiente al índice proporcionado.
    arr_predicciones, etiqueta_real, img = arr_predicciones[i], etiquetas_reales[i], imagenes[i]
    # Configura la gráfica sin líneas de cuadrícula y sin marcas en los ejes x e y.
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    # Muestra la imagen en escala de grises.
    plt.imshow(img[...,0], cmap=plt.cm.binary)

    # Determina la etiqueta de la predicción basada en el valor máximo del arreglo de predicciones.
    etiqueta_prediccion = np.argmax(arr_predicciones)
    # Si la predicción coincide con la etiqueta real, usa el color azul; si no, rojo.
    if etiqueta_prediccion == etiqueta_real:
        color = 'blue'
    else:
        color = 'red'

    # Etiqueta la imagen con el nombre de la clase predicha, el porcentaje de confianza y el nombre real de la clase.
    plt.xlabel("{} {:2.0f}% ({})".format(nombres_clases[etiqueta_prediccion],
                                    100*np.max(arr_predicciones),
                                    nombres_clases[etiqueta_real]),
                                    color=color)

# Define una función para graficar el arreglo de valores de las predicciones.
def graficar_valor_arreglo(i, arr_predicciones, etiqueta_real):
    # Extrae la predicción y la etiqueta real correspondiente al índice proporcionado.
    arr_predicciones, etiqueta_real = arr_predicciones[i], etiqueta_real[i]
    # Configura la gráfica sin líneas de cuadrícula y sin marcas en los ejes x e y.
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
        # Crea una gráfica de barras para las predicciones con un color gris por defecto.
    grafica = plt.bar(range(10), arr_predicciones, color="#777777")
    # Establece el límite del eje y de la gráfica entre 0 y 1.
    plt.ylim([0, 1]) 
    # Determina la etiqueta de la predicción basada en el valor máximo del arreglo de predicciones.
    etiqueta_prediccion = np.argmax(arr_predicciones)
    
    # Cambia el color de la barra correspondiente a la predicción a rojo y la real a azul.
    grafica[etiqueta_prediccion].set_color('red')
    grafica[etiqueta_real].set_color('blue')
  
# Establece el número de filas y columnas para mostrar las imágenes y sus gráficas de barras asociadas.
filas = 5
columnas = 5
# Calcula el número total de imágenes a mostrar basado en las filas y columnas definidas.
num_imagenes = filas*columnas
# Configura el tamaño de la figura para la visualización de todas las imágenes y gráficas.
plt.figure(figsize=(2*2*columnas, 2*filas))
# Itera sobre el número total de imágenes a mostrar.
for i in range(num_imagenes):
    # Crea un subgráfico para la imagen en la posición correspondiente.
    plt.subplot(filas, 2*columnas, 2*i+1)
    # Llama a la función para graficar la imagen con sus predicciones y etiquetas reales.
    graficar_imagen(i, predicciones, etiquetas_prueba, imagenes_prueba)
    # Crea un subgráfico para la gráfica de barras en la posición correspondiente.
    plt.subplot(filas, 2*columnas, 2*i+2)
    # Llama a la función para graficar la gráfica de barras con las predicciones y etiqueta real.
    graficar_valor_arreglo(i, predicciones, etiquetas_prueba)
plt.show()

######################################
# Imagen de prueba                   #
######################################

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
prediccion = modelo.predict(imagen)
print("Prediccion: " + nombres_clases[np.argmax(prediccion[0])])

#############################################

# Supongamos que 'modelo' es tu modelo entrenado
modelo.save('modelo_ropa.h5')
