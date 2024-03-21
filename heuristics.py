class Heuristics:
    
    @staticmethod
    def capas_resueltas(cubo):
        # Definimos los estados resueltos de cada cara del cubo
        estados_resueltos = [
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  # Cara 1 - Amarillo
            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],  # Cara 2 - Blanco
            [[3, 3, 3], [3, 3, 3], [3, 3, 3]],  # Cara 3 - Naranja
            [[4, 4, 4], [4, 4, 4], [4, 4, 4]],  # Cara 4 - Azul
            [[5, 5, 5], [5, 5, 5], [5, 5, 5]],  # Cara 5 - Rojo
            [[6, 6, 6], [6, 6, 6], [6, 6, 6]]   # Cara 6 - Verde
        ]

        # Calculamos la distancia de cada cara al estado resuelto
        distancia_total = 0
        for cara_actual, estado_resuelto in zip(cubo, estados_resueltos):
            distancia_cara = 0
            for i in range(3):
                for j in range(3):
                    if cara_actual[i][j] != estado_resuelto[i][j]:
                        distancia_cara += 1
            distancia_total += distancia_cara
        return distancia_total