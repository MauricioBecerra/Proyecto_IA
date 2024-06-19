### Mauricio Becerra Guzman - 21310105 ###
import heapq
import os

def create_initial_runs(input_file, run_size, output_dir):
    # Crea el directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    run_index = 0
    with open(input_file, 'r') as file:
        lines = file.readlines()
        # Divide el archivo en runs de tamaño run_size, los ordena y los guarda en archivos separados
        for i in range(0, len(lines), run_size):
            current_run = lines[i:i + run_size]
            current_run.sort()
            run_file = os.path.join(output_dir, f'run_{run_index}.txt')
            with open(run_file, 'w') as run:
                run.writelines(current_run)
            run_index += 1

def merge_files(input_files, output_file):
    min_heap = []
    file_pointers = []
    
    # Abrir todos los archivos y leer la primera línea de cada uno
    for i, file in enumerate(input_files):
        f = open(file, 'r')
        file_pointers.append(f)
        line = f.readline()
        if line:
            heapq.heappush(min_heap, (line, i))

    # Fusionar los archivos ordenados usando un heap de mínimos
    with open(output_file, 'w') as output:
        while min_heap:
            # Extraer el elemento mínimo del heap y escribirlo en el archivo de salida
            min_line, file_index = heapq.heappop(min_heap)
            output.write(min_line)
            
            # Leer la siguiente línea del archivo correspondiente y actualizar el heap
            next_line = file_pointers[file_index].readline()
            if next_line:
                heapq.heappush(min_heap, (next_line, file_index))
    
    # Cerrar todos los archivos abiertos
    for f in file_pointers:
        f.close()

def external_sort(input_file, output_file, run_size, num_ways):
    # Directorio donde se guardarán los runs temporales
    run_dir = 'runs'
    create_initial_runs(input_file, run_size, run_dir)
    
    # Obtener la lista de archivos de runs
    run_files = [os.path.join(run_dir, f) for f in os.listdir(run_dir)]
    
    # Fusionar los archivos de runs en el archivo de salida final
    merge_files(run_files, output_file)
    
    # Eliminar los archivos temporales de runs y el directorio
    for file in run_files:
        os.remove(file)
    os.rmdir(run_dir)

# Crear un archivo de prueba con números del 1000 al 1
with open('data.txt', 'w') as f:
    f.writelines(f"{i}\n" for i in range(1000, 0, -1))

# Definir los parámetros y llamar a external_sort para ordenar el archivo de prueba
input_file = 'data.txt'
output_file = 'sorted_data.txt'
run_size = 100  # Tamaño de cada run
num_ways = 10   # Número de vías para la fusión (no utilizado en esta implementación básica)

external_sort(input_file, output_file, run_size, num_ways)
