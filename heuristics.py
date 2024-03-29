class Heuristics:
    
    @staticmethod
    def capas_resueltas(cubo):
        #Solved cube
        estados_resueltos = [
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  # Cara 1 - Yellow
            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],  # Cara 2 - White
            [[3, 3, 3], [3, 3, 3], [3, 3, 3]],  # Cara 3 - Orange
            [[4, 4, 4], [4, 4, 4], [4, 4, 4]],  # Cara 4 - Blue
            [[5, 5, 5], [5, 5, 5], [5, 5, 5]],  # Cara 5 - Red
            [[6, 6, 6], [6, 6, 6], [6, 6, 6]]   # Cara 6 - Green
        ]

        #Distance between the state and the solved state
        distancia_total = 0
        for cara_actual, estado_resuelto in zip(cubo, estados_resueltos):
            distancia_cara = 0
            for i in range(3):
                for j in range(3):
                    if cara_actual[i][j] != estado_resuelto[i][j]:
                        distancia_cara += 1
            distancia_total += distancia_cara
        return distancia_total