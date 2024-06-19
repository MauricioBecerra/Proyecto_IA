### Mauricio Becerra Guzman - 21310105 ###
def counting_sort(arr, exp):
    # Crear un array para contar las ocurrencias de cada dígito (0-9)
    count = [0] * 10
    # Crear un array para almacenar temporalmente el resultado ordenado
    output = [0] * len(arr)

    # Contar el número de ocurrencias de cada dígito en la posición exp
    for i in range(len(arr)):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Modificar count[i] para que contenga la posición de este dígito en output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el array output usando count para ubicar los elementos
    for i in range(len(arr) - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copiar el array output al array original arr, para que arr contenga los números ordenados según el dígito actual
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Encontrar el número máximo para saber el número de dígitos
    max1 = max(arr)
    exp = 1
    # Aplicar counting_sort para cada dígito. Empezamos con el dígito menos significativo.
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ejemplo de uso
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Array original:")
print(arr)

radix_sort(arr)

print("Array ordenado:")
print(arr)