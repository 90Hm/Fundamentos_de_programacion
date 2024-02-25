# En este segundo ejercicio utilizaremos una matriz bidimensional (3x3) con nombres de frutas de mi preferencia
Asignacion_de_frutas = [
    ['manzana', 'pera', 'uva'],
    ['durazno', 'kiwi', 'mango'],
    ['piña', 'fresa', 'sandía']
]

def buscar_fruta(Asignacion_de_frutas, fruta):
    for fila in range(len(Asignacion_de_frutas)):
        for columna in range(len(Asignacion_de_frutas[0])):
            if Asignacion_de_frutas[fila][columna] == fruta:
                return True, fila, columna
    return False, None, None

#Agregamos el nombre de la fruta que deseamos buscar
fruta_a_buscar = 'sandía'

# Este punto es importante ya que hara que se ejecute la busqueda
encontrada, fila, columna = buscar_fruta(Asignacion_de_frutas, fruta_a_buscar)

# Este apartado mostrara el resultado de la búsqueda de la fruta asignada a buscar
if encontrada:
    print(f"La fruta mencionada '{fruta_a_buscar}' se encontró en la posición de la tabla [{fila}][{columna}] de la matriz.")
else:
    print(f"La fruta mencionada'{fruta_a_buscar}' no se encontra dentro de la matriz.")
