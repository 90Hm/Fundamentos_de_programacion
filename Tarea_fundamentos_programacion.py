#Búsqueda y Ordenación en Arreglos Multidimensionales
# En este primer ejercicio utilizaremos una matriz bidimensional (3x3) con valores numéricos
a = [
    [10, 11, 12],
    [13,14, 15],
    [16, 17, 18]
]

# Función de búsqueda del valor
def buscar_valor(a, valor):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == valor:
                return True, i, j
    return False, None, None

# Valor a buscar
valor_a_buscar = 10

# Iniciamos la busqueda
encontrado, fila, columna = buscar_valor(a,valor_a_buscar)

# Imprimimos el resultado
if encontrado:
    print(f"El valor asignado {valor_a_buscar} se encuentra en la posición [{fila}][{columna}] de la matriz.")

else:
    print(f"El valor asignado {valor_a_buscar} no se encontró en la matriz.")