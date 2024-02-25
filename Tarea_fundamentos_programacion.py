#Búsqueda y Ordenación en Arreglos Multidimensionales
# Definir una matriz bidimensional (3x3) con valores numéricos
matriz = [
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return True, i, j
    return False, None, None

# Valor a buscar
valor_a_buscar = 15

# Realizar la búsqueda
encontrado, fila, columna = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la posición [{fila}][{columna}] de la matriz.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
