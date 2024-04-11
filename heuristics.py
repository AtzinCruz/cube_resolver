import copy
class Heuristics:
    
    estados_resueltos = [
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  # Cara 1 - Yellow
            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],  # Cara 2 - White
            [[3, 3, 3], [3, 3, 3], [3, 3, 3]],  # Cara 3 - Orange
            [[4, 4, 4], [4, 4, 4], [4, 4, 4]],  # Cara 4 - Blue
            [[5, 5, 5], [5, 5, 5], [5, 5, 5]],  # Cara 5 - Red
            [[6, 6, 6], [6, 6, 6], [6, 6, 6]]   # Cara 6 - Green
        ]

    @staticmethod
    def capas_resueltas(cubo):

        #Distance between the state and the solved state
        distancia_total = 0
        for cara_actual, estado_resuelto in zip(cubo, Heuristics.estados_resueltos):
            distancia_cara = 0
            for i in range(3):
                for j in range(3):
                    if cara_actual[i][j] != estado_resuelto[i][j]:
                        distancia_cara += 1
            distancia_total += distancia_cara
        return distancia_total
    
    @staticmethod
    def bloques_correctos(cubo):
        #Distance between the state and the solved state
        bloques_correctos = 0
        for cara_actual, estado_resuelto in zip(cubo, Heuristics.estados_resueltos):
            for i in range(3):
                for j in range(3):
                    if cara_actual[i][j] == estado_resuelto[i][j]:
                        bloques_correctos += 1
        return bloques_correctos * -1
    
    @staticmethod
    #Distance between the correct position and the position on the matrix
    def Manhattan_distance(cube):
        total_distance = 0
        for face_idx, face in enumerate(cube):
            for row_idx, row in enumerate(face):
                for col_idx, color in enumerate(row):
                    if color != Heuristics.estados_resueltos[face_idx][row_idx][col_idx]:
                        # Calcular la distancia de Manhattan para la pieza actual
                        distance = abs(face_idx - Heuristics.estados_resueltos[face_idx][row_idx][0]) + abs(row_idx - Heuristics.estados_resueltos[face_idx][row_idx][1]) + abs(col_idx - Heuristics.estados_resueltos[face_idx][row_idx][2])
                        total_distance += distance
        
        return total_distance
    
    
    @staticmethod
    #Check if the corners are in the correct spot
    def esquinas_correctas(cubo):
        sum = 0
        for cara_actual, estado_resuelto in zip(cubo, Heuristics.estados_resueltos):
            corners = [[0, 0],[0, 2], [2, 0], [2, 2]]
            for c1 in corners:
                c1_value = cara_actual[c1[0]][c1[1]]
                c2_value = estado_resuelto[c1[0]][c1[1]]
                if(c1_value == c2_value):
                    sum += 1
        return sum * -1

        

        