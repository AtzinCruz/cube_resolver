class cube:
    cubo = [
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  # Lado 1
        [[2, 2, 2], [2, 2, 2], [2, 2, 2]],  # Lado 2
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]],  # Lado 3
        [[4, 4, 4], [4, 4, 4], [4, 4, 4]],  # Lado 4
        [[5, 5, 5], [5, 5, 5], [5, 5, 5]],  # Lado 5
        [[6, 6, 6], [6, 6, 6], [6, 6, 6]]   # Lado 6
    ]

# Función para imprimir el cubo
def imprimir_cubo(cubo):
    for lado in cubo:
        for fila in lado:
            print(fila)
        print()

# Imprimir el cubo
cubo = cube()
imprimir_cubo(cubo)
