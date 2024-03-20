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
            self.cubo[movements[1]][2][i] = self.cubo[movements[2]][2 -i][2]
        for i in range(3):
            self.cubo[movements[2]][i][2] = self.cubo[movements[3]][0][i]
        for i in range(3):
            aux = aux[::-1]
            self.cubo[movements[3]][0][i] = aux[i]
    
    def movement_b(self):
        self.cubo[5] = self.rotar_contra_reloj(self.cubo[5])
        movements = [1, 2, 0, 4]
        aux = [self.cubo[movements[0]][2][j] for j in range(3)]  # Corregido el rango
        for i in range(3):
            self.cubo[movements[0]][2][i] = self.cubo[movements[1]][i][0]
        for i in range(3):
            self.cubo[movements[1]][i][0] = self.cubo[movements[2]][0][2 - i]
        for i in range(3):
            self.cubo[movements[2]][0][i] = self.cubo[movements[3]][i][2]
        for i in range(3):
            aux = aux[::-1]
            self.cubo[movements[3]][i][2] = aux[i]
        

    
class Solver:
    def __init__(self):
        self.pattern = {
            1 : [[0, 2, 0],
                 [2, 2, 2],
                 [0, 2, 0]],
            2: []
        }


# Función para imprimir el cubo
def imprimir_cubo(cubo):
    for lado in cubo:
        for fila in lado:
            print(fila)
        print()


def revolver_igual(cubo, movement_a, movement_b):
    for i in range(6):
        print(f"Movimiento numero:{i + 1}")
        cubo.move_manual(movement_a)
        cubo.move_manual(movement_a)
        cubo.move_manual(movement_a)
        cubo.move_manual(movement_b)
        cubo.move_manual(movement_a)
        cubo.move_manual(movement_b)
        cubo.move_manual(movement_b)
        cubo.move_manual(movement_b)
        imprimir_cubo(cubo.cubo)

# Imprimir el cubo
cubo = Cube()
imprimir_cubo(cubo.cubo)
print('After movements:')
imprimir_cubo(cubo.cubo)
revolver_igual(cubo, 'F', 'D')
print('After movements:')
imprimir_cubo(cubo.cubo)