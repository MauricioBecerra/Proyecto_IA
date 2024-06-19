### Mauricio Becerra Guzman - 21310105 ###

def selection_sort(arr):
    """
    Función para ordenar una lista usando el algoritmo de selección.

    :param arr: Lista de elementos a ordenar.
    """
    # Obtenemos el tamaño de la lista.
    n = len(arr)
    
    # Iteramos sobre cada elemento de la lista.
    for i in range(n):
        # Suponemos que el primer elemento no ordenado es el menor.
        min_idx = i
        
        # Iteramos sobre los elementos restantes para encontrar el menor.
        for j in range(i + 1, n):
            # Si encontramos un elemento menor, actualizamos min_idx.
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Si encontramos un nuevo elemento menor, lo intercambiamos con el elemento actual.
        # Esta operación pone al menor elemento en su posición correcta.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Mostramos el estado actual de la lista después de cada intercambio.
        print(f"Iteración {i + 1}: {arr}")

# Lista de ejemplo para ordenar.
example_list = [15, 17, 0, 1, 3]

# Llamamos a la función de ordenamiento.
selection_sort(example_list)

# Mostramos la lista ordenada final.
print("Lista ordenada: ", example_list)
