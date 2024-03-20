from collections import deque
import copy
from heapq import heappop, heappush

class Cube:
    def __init__(self):
        self.cubo = [
            [[1, 1, 1], 
             [1, 1, 1], 
             [1, 1, 1]],  # Lado 1 - Amarillo

            [[2, 2, 2], 
             [2, 2, 2], 
             [2, 2, 2]],  # Lado 2 - Blanco

            [[3, 3, 3], 
             [3, 3, 3], 
             [3, 3, 3]],  # Lado 3 - Naranja

            [[4, 4, 4], 
             [4, 4, 4], 
             [4, 4, 4]],  # Lado 4 - Azul

            [[5, 5, 5], 
             [5, 5, 5], 
             [5, 5, 5]],  # Lado 5 - Rojo
             
            [[6, 6, 6], 
             [6, 6, 6], 
             [6, 6, 6]]   # Lado 6 - Verde
        ]

        self.cubo_resuelto = copy.deepcopy(self.cubo)
        self.movements = {
            'U' : self.movement_u,
            'D' : self.movement_d,
            'L' : self.movement_l,
            'R' : self.movement_r,
            'F' : self.movement_f,
            'B' : self.movement_b
        }
        self.last_move = None
        self.last_move_count = 0


    def move_manual(self, mov):
        if mov in self.movements:
            self.movements[mov]()
        else:
            print("Movimiento no disponible")
    
    def move(self, mov):
        if mov in self.movements:
            # Verificar si el movimiento actual es el mismo que el último movimiento
            if mov == self.last_move:
                self.last_move_count += 1
                if self.last_move_count >= 3:
                    print("Se ha realizado el mismo movimiento {} veces consecutivas. No se puede realizar más.".format(self.last_move_count))
                    return
            else:
                self.last_move = mov
                self.last_move_count = 1

            self.movements[mov]()
        else:
            print("Movimiento no disponible")
    
    @staticmethod
    def rotar_contra_reloj(matriz):
        # Intercambiar filas
        matriz = matriz[::-1]
        # Transponer la matriz
        matriz_rotada = [list(x) for x in zip(*matriz)]
        return matriz_rotada

    # Movimientos donde se centrará todo será en el azul - con la cara amarilla arriba
    def movement_u(self):
        self.cubo[0] = self.rotar_contra_reloj(self.cubo[0])
        movements = [2, 3, 4, 5]
        aux = self.cubo[movements[0]][0][::-1]
        self.cubo[movements[0]][0] = self.cubo[movements[1]][0]
        self.cubo[movements[1]][0] = self.cubo[movements[2]][0]
        self.cubo[movements[2]][0] = self.cubo[movements[3]][2][::-1]
        self.cubo[movements[3]][2] = aux
    
    def movement_d(self):
        self.cubo[1] = self.rotar_contra_reloj(self.cubo[1])
        movements = [4, 3, 2, 5]
        aux = self.cubo[movements[0]][2][::-1]
        self.cubo[movements[0]][2] = self.cubo[movements[1]][2]
        self.cubo[movements[1]][2] = self.cubo[movements[2]][2]
        self.cubo[movements[2]][2] = self.cubo[movements[3]][0][::-1]
        self.cubo[movements[3]][0] = aux
    
    def movement_l(self):
        self.cubo[2] = self.rotar_contra_reloj(self.cubo[2])
        movements = [0, 5, 1, 3]
        aux = [self.cubo[movements[0]][j][0] for j in range(3)]  # Corregido el rango
        for i in range(3):
            for j in range(3):  # Cambiado a rango(3) para evitar errores de índice
                self.cubo[movements[i]][j][0] = self.cubo[movements[i + 1]][j][0]
        for j in range(3):  # Cambiado a rango(3) para evitar errores de índice
            self.cubo[movements[3]][j][0] = aux[j]
    
    def movement_r(self):
        self.cubo[4] = self.rotar_contra_reloj(self.cubo[4])
        movements = [3, 1, 5 ,0]
        aux = [self.cubo[movements[0]][j][2] for j in range(3)]  # Corregido el rango
        for i in range(3):
            for j in range(3):  # Cambiado a rango(3) para evitar errores de índice
                self.cubo[movements[i]][j][2] = self.cubo[movements[i + 1]][j][2]
        for j in range(3):  # Cambiado a rango(3) para evitar errores de índice
            self.cubo[movements[3]][j][2] = aux[j]
    
    def movement_f(self):
        self.cubo[3] = self.rotar_contra_reloj(self.cubo[3])
        movements = [4, 0, 2, 1]
        aux = [self.cubo[movements[0]][j][0] for j in range(3)]  # Corregido el rango
        for i in range(3):
            self.cubo[movements[0]][i][0] = self.cubo[movements[1]][2][i]
        for i in range(3):
            self.cubo[movements[1]][2][i] = self.cubo[movements[2]][i][2]
        for i in range(3):
            self.cubo[movements[2]][i][2] = self.cubo[movements[3]][0][i]
        for i in range(3):
            self.cubo[movements[3]][0][i] = aux[i]
    
    def movement_b(self):
        self.cubo[5] = self.rotar_contra_reloj(self.cubo[5])
        movements = [1, 2, 0, 4]
        aux = [self.cubo[movements[0]][2][j] for j in range(3)]  # Corregido el rango
        for i in range(3):
            self.cubo[movements[0]][2][i] = self.cubo[movements[1]][i][0]
        for i in range(3):
            self.cubo[movements[1]][i][0] = self.cubo[movements[2]][0][i]
        for i in range(3):
            self.cubo[movements[2]][0][i] = self.cubo[movements[3]][i][2]
        for i in range(3):
            self.cubo[movements[3]][i][2] = aux[i]
        

    
    def manhattan_distance(self):
        distance = 0
        # Define la configuración deseada para cada cara del cubo
        desired_configurations = [
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  # Amarillo
            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],  # Blanco
            [[3, 3, 3], [3, 3, 3], [3, 3, 3]],  # Naranja
            [[4, 4, 4], [4, 4, 4], [4, 4, 4]],  # Azul
            [[5, 5, 5], [5, 5, 5], [5, 5, 5]],  # Rojo
            [[6, 6, 6], [6, 6, 6], [6, 6, 6]]   # Verde
        ]

        # Calcula la distancia de Manhattan para cada cara del cubo
        for current_face, desired_face in zip(self.cubo, desired_configurations):
            for i in range(3):
                for j in range(3):
                    if current_face[i][j] != desired_face[i][j]:
                        distance += abs(i - 1) + abs(j - 1)  # Suma las distancias horizontales y verticales
    
        return distance

    def solve_bfs(self):
        # Definir la representación de un estado del cubo
        class CubeState:
            def __init__(self, cube, moves=[], move_count=0):
                self.cube = cube
                self.moves = moves
                self.move_count = move_count

            def __lt__(self, other):
                return self.move_count < other.move_count

        # Cola para almacenar los estados del cubo que se van explorando
        priority_queue = []

        # Conjunto para almacenar los estados del cubo ya visitados
        visited = set()

        # Movimientos permitidos
        moves = list(self.movements.keys())

        # Estado inicial del cubo
        initial_state = CubeState(self, [], 0)

        # Agregar el estado inicial a la cola
        heappush(priority_queue, initial_state)

        while priority_queue:
            current_state = heappop(priority_queue)
            current_cube = current_state.cube

            # Comprobar si el estado actual es el estado objetivo
            if current_cube.cubo == self.cubo_resuelto:
                print("Solución encontrada en {} movimientos:".format(len(current_state.moves)))
                for move in current_state.moves:
                    print(move)
                return

            # Marcar el estado actual como visitado
            visited.add(str(current_cube.cubo))

            # Si el estado actual no es el objetivo, generar los siguientes estados posibles
            for move in moves:
                new_cube = Cube()  # Crear un nuevo objeto Cube
                new_cube.cubo = [list(face) for face in current_cube.cubo]  # Copiar las caras del cubo
                new_moves = current_state.moves + [move]

                # Realizar el movimiento en el nuevo estado
                new_cube.move(move)

                # Verificar si se han realizado más de 3 movimientos consecutivos
                if len(new_moves) > 3 and new_moves[-3:] == [move] * 3:
                    continue

                # Crear un nuevo estado
                new_state = CubeState(new_cube, new_moves, current_state.move_count + 1)

                # Comprobar si el nuevo estado ya ha sido visitado
                if str(new_state.cube.cubo) not in visited:
                    heappush(priority_queue, new_state)

        print("No se encontró solución.")

# Función para imprimir el cubo
def imprimir_cubo(cubo):
    for lado in cubo:
        for fila in lado:
            print(fila)
        print()


def revolver_igual(cubo):
    for i in range(6):
        cubo.move_manual('U')
        cubo.move_manual('U')
        cubo.move_manual('U')
        cubo.move_manual('R')
        cubo.move_manual('U')
        cubo.move_manual('R')
        cubo.move_manual('R')
        cubo.move_manual('R')
# Imprimir el cubo
cubo = Cube()
imprimir_cubo(cubo.cubo)
revolver_igual(cubo)
print('After movements:')
imprimir_cubo(cubo.cubo)