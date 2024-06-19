### Mauricio Becerra Guzman - 21310105 ###
def insertion_sort(arr):
    """
    Función de ordenamiento por inserción que recibe una lista 'arr' como argumento
    y la ordena en su lugar.
    """
    # Itera sobre el arreglo desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        # 'key' es el valor del elemento en la posición 'i' que se va a insertar en el subarreglo ordenado
        key = arr[i]
        
        # Inicializa 'j' como el índice del elemento anterior al actual
        j = i - 1
        
        # Mueve los elementos del arreglo que son mayores que 'key' a una posición adelante de su posición actual
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Inserta 'key' en la posición correcta dentro del subarreglo ordenado
        arr[j + 1] = key

# Ejemplo de uso
if __name__ == "__main__":
    # Define un arreglo de ejemplo para ser ordenado
    arr = [15, 17, 0, 1, 3]

    # Imprime el arreglo original
    print("Arreglo original:", arr)

    # Llama a la función de ordenamiento por inserción para ordenar el arreglo
    insertion_sort(arr)

    # Imprime el arreglo ordenado
    print("Arreglo ordenado:", arr)
