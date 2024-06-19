### Mauricio Becerra Guzman - 21310105 ###
def bubble_sort(arr):
    """
    Función para ordenar una lista usando el algoritmo de ordenamiento de burbuja.
    
    :param arr: Lista de elementos a ordenar.
    :return: Lista ordenada (opcional, ya que la lista se ordena en su lugar).
    """
    # Obtenemos la longitud de la lista.
    n = len(arr)
    
    # Iteramos a través de todos los elementos de la lista.
    for i in range(n):
        # Dentro del primer bucle, iteramos desde el principio de la lista hasta el penúltimo elemento no ordenado.
        for j in range(0, n - i - 1):
            # Comparamos el elemento actual con el siguiente.
            if arr[j] > arr[j + 1]:
                # Si el elemento actual es mayor que el siguiente, los intercambiamos.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Aquí utilizamos la técnica de desempaquetado para intercambiar los valores.
        
        # Imprimimos el estado de la lista después de cada iteración del primer bucle para ver el progreso.
        print(f"Iteración {i + 1}: {arr}")
        
    # Devolvemos la lista ordenada (esto es opcional ya que la lista se ordena en su lugar).
    return arr

# Lista de ejemplo a ordenar.
lista = [64, 34, 25, 12, 22, 11, 90]

# Imprimimos la lista original.
print("Lista original:", lista)

# Llamamos a la función bubble_sort pasando la lista de ejemplo.
sorted_lista = bubble_sort(lista)

# Imprimimos la lista ordenada.
print("Lista ordenada:", sorted_lista)