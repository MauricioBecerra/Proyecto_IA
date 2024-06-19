### Mauricio Becerra Guzman - 21310105 ###
class TreeNode:
    def __init__(self, value):
        self.value = value  # Valor del nodo
        self.left = None    # Hijo izquierdo del nodo
        self.right = None   # Hijo derecho del nodo

def insert(root, value):
    """
    Función para insertar un valor en un árbol binario de búsqueda.

    :param root: Nodo raíz del árbol.
    :param value: Valor a insertar.
    :return: Nodo raíz actualizado después de la inserción.
    """
    if root is None:
        return TreeNode(value)  # Si el árbol está vacío, crea un nuevo nodo con el valor dado
    else:
        if value < root.value:
            root.left = insert(root.left, value)  # Inserta en el subárbol izquierdo si el valor es menor que el valor del nodo
        else:
            root.right = insert(root.right, value)  # Inserta en el subárbol derecho si el valor es mayor o igual al valor del nodo
    return root

def inorder_traversal(root, result):
    """
    Realiza un recorrido en orden del árbol binario de búsqueda y llena una lista con los valores ordenados.

    :param root: Nodo raíz del árbol.
    :param result: Lista para almacenar los valores ordenados.
    """
    if root is not None:
        inorder_traversal(root.left, result)    # Recorre el subárbol izquierdo en orden
        result.append(root.value)               # Agrega el valor del nodo actual a la lista de resultados
        inorder_traversal(root.right, result)   # Recorre el subárbol derecho en orden

def tree_sort(arr):
    """
    Función principal para ordenar una lista utilizando Tree Sort.

    :param arr: Lista de elementos a ordenar.
    :return: Lista ordenada.
    """
    if not arr:
        return []  # Si el arreglo está vacío, devuelve una lista vacía

    root = TreeNode(arr[0])  # Crea el nodo raíz con el primer elemento del arreglo
    for value in arr[1:]:
        insert(root, value)  # Inserta el resto de los elementos en el árbol

    sorted_arr = []
    inorder_traversal(root, sorted_arr)  # Realiza un recorrido en orden del árbol y llena sorted_arr con los elementos ordenados
    return sorted_arr

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [5, 3, 7, 2, 4, 8, 1]
    print("Array original:", arr)
    sorted_arr = tree_sort(arr)
    print("Array ordenado:", sorted_arr)
