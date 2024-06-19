### Mauricio Becerra Guzman - 21310105 ###
import heapq  # Importamos heapq para manejar una cola de prioridad (min-heap)
import os     # Importamos os para operaciones del sistema de archivos

def polyphase_sort(input_file, output_file, temp_dir, num_files):
    """
    Funcion principal para realizar el ordenamiento Polyphase.
    input_file: archivo de entrada con datos desordenados.
    output_file: archivo de salida para datos ordenados.
    temp_dir: directorio temporal para archivos intermedios.
    num_files: numero de archivos temporales a usar.
    """

    # Funcion para dividir el archivo de entrada en runas (subsecuencias ordenadas)
    def create_initial_runs():
        """
        Divide el archivo de entrada en varias sub-listas (runs) ordenadas y las guarda en archivos temporales.
        """
        runs = []  # Lista para almacenar los nombres de los archivos temporales
        with open(input_file, 'r') as f:
            data = f.readlines()
            chunk_size = len(data) // num_files + 1  # Calcula el tamano de cada runa
            for i in range(num_files):
                chunk = data[i * chunk_size:(i + 1) * chunk_size]  # Selecciona la porcion de datos para la runa actual
                chunk.sort()  # Ordena la runa
                temp_filename = os.path.join(temp_dir, f'temp_run_{i}.txt')  # Nombre del archivo temporal
                with open(temp_filename, 'w') as temp_file:
                    temp_file.writelines(chunk)  # Escribe la runa ordenada en el archivo temporal
                runs.append(temp_filename)  # Agrega el nombre del archivo temporal a la lista de runs
        return runs  # Retorna la lista de nombres de archivos temporales (runs)

    # Funcion para fusionar las runas en el archivo de salida
    def merge_runs(runs):
        """
        Fusiona las runas ordenadas almacenadas en archivos temporales en el archivo de salida ordenado.
        """
        min_heap = []  # Min-heap para seleccionar el siguiente elemento mas pequeno
        file_handlers = [open(run, 'r') for run in runs]  # Lista de manejadores de archivos temporales abiertos

        # Inicializa el heap con el primer elemento de cada runa
        for i, fh in enumerate(file_handlers):
            line = fh.readline().strip()  # Lee la primera linea de la runa y elimina el salto de linea
            if line:
                heapq.heappush(min_heap, (line, i))  # Agrega el elemento al heap con su indice de runa

        with open(output_file, 'w') as out_file:
            while min_heap:
                smallest, i = heapq.heappop(min_heap)  # Extrae el elemento mas pequeno del heap
                out_file.write(smallest + '\n')  # Escribe el elemento en el archivo de salida
                next_line = file_handlers[i].readline().strip()  # Lee la siguiente linea de la runa correspondiente
                if next_line:
                    heapq.heappush(min_heap, (next_line, i))  # Agrega el siguiente elemento al heap

        # Cierra todos los archivos temporales
        for fh in file_handlers:
            fh.close()

    runs = create_initial_runs()  # Crea las runas iniciales divididas y ordenadas
    merge_runs(runs)  # Fusiona las runas ordenadas en el archivo de salida

    # Elimina los archivos temporales (runs)
    for run in runs:
        os.remove(run)

input_file = 'input.txt'  # Nombre del archivo de entrada
output_file = 'sorted_output.txt'  # Nombre del archivo de salida ordenado
temp_dir = 'temp_files'  # Directorio para almacenar archivos temporales (runs)
num_files = 3  # Numero de archivos temporales (runs) a utilizar

# Crea un archivo de entrada de ejemplo si no existe
if not os.path.exists(input_file):
    with open(input_file, 'w') as f:
        f.writelines(f"{i}\n" for i in range(100, 0, -1))  # Escribe numeros del 100 al 1 en el archivo

# Crea el directorio temporal si no existe
os.makedirs(temp_dir, exist_ok=True)

# Llama a la funcion de ordenamiento Polyphase
polyphase_sort(input_file, output_file, temp_dir, num_files)

# Elimina el directorio temporal luego de usarlo
os.rmdir(temp_dir)
