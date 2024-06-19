### Mauricio Becerra Guzman - 21310105 ###
import os
import heapq

def distribution_of_initial_runs(input_file, temp_dir, run_size):
    """
    Distribuye las corridas iniciales en archivos temporales
    """
    # Verifica si el archivo de entrada existe
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"El archivo {input_file} no existe.")

    # Lee el archivo de entrada y crea y guarda los runs ordenados en archivos temporales
    with open(input_file, 'r') as infile:
        run = []
        run_num = 0
        
        for line in infile:
            run.append(int(line.strip()))  # Lee y agrega cada linea al run actual
            if len(run) == run_size:
                run.sort()  # Ordena el run actual
                with open(os.path.join(temp_dir, f'run_{run_num}.txt'), 'w') as outfile:
                    for item in run:
                        outfile.write(f'{item}\n')  # Escribe el run ordenado a un archivo temporal
                run = []
                run_num += 1
        
        if run:
            run.sort()  # Ordena y escribe el ultimo run si no esta vacio
            with open(os.path.join(temp_dir, f'run_{run_num}.txt'), 'w') as outfile:
                for item in run:
                    outfile.write(f'{item}\n')

def merge_runs(temp_dir, output_file, num_runs):
    """
    Mezcla los runs ordenados en el archivo de salida
    """
    # Abre todos los archivos de runs y los inicializa en un min-heap
    run_files = [open(os.path.join(temp_dir, f'run_{i}.txt'), 'r') for i in range(num_runs)]
    output = open(output_file, 'w')
    
    min_heap = []
    
    # Inicializa el heap con el primer elemento de cada run
    for i, f in enumerate(run_files):
        line = f.readline().strip()
        if line:
            heapq.heappush(min_heap, (int(line), i))
    
    # Fusiona los runs ordenadamente extrayendo el elemento mas pequeno del heap
    while min_heap:
        smallest, run_index = heapq.heappop(min_heap)
        output.write(f'{smallest}\n')
        
        line = run_files[run_index].readline().strip()
        if line:
            heapq.heappush(min_heap, (int(line), run_index))
    
    # Cierra todos los archivos abiertos
    for f in run_files:
        f.close()
    output.close()

def external_sort(input_file, output_file, temp_dir, run_size):
    """
    Realiza el ordenamiento externo
    """
    # Crea el directorio temporal si no existe
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Distribuye los runs iniciales en archivos temporales
    distribution_of_initial_runs(input_file, temp_dir, run_size)
    
    # Cuenta el numero de runs creados en el directorio temporal
    num_runs = len([name for name in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, name))])
    
    # Mezcla los runs para obtener el archivo de salida ordenado
    merge_runs(temp_dir, output_file, num_runs)

# Parametros del ordenamiento externo
input_file = 'C:/ruta/completa/al/archivo/input.txt'  # Especifica la ruta completa si es necesario
output_file = 'C:/ruta/completa/al/archivo/output.txt'
temp_dir = 'C:/ruta/completa/al/directorio/temp'
run_size = 100  # Tamano del run

try:
    external_sort(input_file, output_file, temp_dir, run_size)
except FileNotFoundError as e:
    print(e)
