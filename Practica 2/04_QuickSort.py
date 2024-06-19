### Mauricio Becerra Guzman - 21310105 ###
def quicksort(arr):
    """
    Función principal que ordena un arreglo utilizando el algoritmo QuickSort.

    :param arr: Lista de elementos a ordenar.
    :return: Lista ordenada.
    """
    if len(arr) <= 1:
        return arr  # Si el arreglo tiene 0 o 1 elemento, ya está ordenado

    pivot = arr[-1]  # Elegimos el pivote como el último elemento del arreglo

    left = []   # Lista para los elementos menores o iguales al pivote
    right = []  # Lista para los elementos mayores al pivote

    # Iteramos sobre todos los elementos excepto el pivote
    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)  # Si el elemento es menor o igual al pivote, lo añadimos a la lista izquierda
        else:
            right.append(x)  # Si el elemento es mayor al pivote, lo añadimos a la lista derecha

    # Llamamos recursivamente a quicksort en las sublistas izquierda y derecha,
    # y combinamos los resultados con el pivote en el medio
    return quicksort(left) + [pivot] + quicksort(right)

# Ejemplo de uso
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Array original:", arr)
    sorted_arr = quicksort(arr)
    print("Array ordenado:", sorted_arr)
