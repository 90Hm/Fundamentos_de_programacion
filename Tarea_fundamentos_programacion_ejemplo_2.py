def buscar_fruta(matriz, fruta):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == fruta:
                return True, fila, columna
    return False, None, None


# Definir una matriz bidimensional (3x3) con nombres de frutas
matriz_frutas = [
    ['manzana', 'pera', 'uva'],
    ['durazno', 'kiwi', 'mango'],
    ['piña', 'fresa', 'sandía']
]

# Fruta a buscar
fruta_a_buscar = 'kiwi'

# Ejecutar búsqueda
encontrada, fila, columna = buscar_fruta(matriz_frutas, fruta_a_buscar)

# Mostrar el resultado de la búsqueda
if encontrada:
    print(f"La fruta '{fruta_a_buscar}' se encontró en la posición [{fila}][{columna}] de la matriz.")
else:
    print(f"La fruta '{fruta_a_buscar}' no se encontró en la matriz.")