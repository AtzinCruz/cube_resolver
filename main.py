import time
import random
from cube import Cube
from solvers import Solver
from heuristics import Heuristics
import time

#Print cube in matrix form
def imprimir_cubo(cubo):
    for lado in cubo:
        for fila in lado:
            print(fila)
        print()
    
#Random suffhle

def shuffle_cube(cube, num_moves=20):
    moves = []
    valid_moves = cube.movements.keys()
    for _ in range(num_moves):
        move = random.choice(list(valid_moves))
        cube.move(move)
        moves += move
    return moves

#Manual moves

def caso_prueba1():
    cubo = Cube()
    imprimir_cubo(cubo.cubo)
    cubo.move_manual('B')
    cubo.move_manual('b')
    print('After movements:')
    imprimir_cubo(cubo.cubo)

#BFS 
def caso_prueba2(mov):
    cubo = Cube()
    imprimir_cubo(cubo.cubo)
    print(shuffle_cube(cubo, mov))
    print('After movements:')
    imprimir_cubo(cubo.cubo)
    solver = Solver(cubo)
    flag, path = solver.bfs()
    if flag:
        print(path)
    else:
        print('No se ha encontrado solución')

#BFS_H
def caso_prueba3(mov):
    heuristic = Heuristics.esquinas_correctas
    cubo = Cube()
    imprimir_cubo(cubo.cubo)
    print(shuffle_cube(cubo, mov))
    print('After movements:')
    imprimir_cubo(cubo.cubo)
    solver = Solver(cubo)
    flag, path = solver.bfs_h(heuristic)
    if flag:
        print(path)
    else:
        print('No se ha encontrado solución')

#A*
def caso_prueba4(mov):
    heuristics = Heuristics.esquinas_correctas
    cubo = Cube()
    imprimir_cubo(cubo.cubo)
    print(shuffle_cube(cubo, mov))
    print('After movements:')
    imprimir_cubo(cubo.cubo)
    solver = Solver(cubo)
    path = solver.A_star(heuristics)
    if path:
        print(path)
        return len(path)
    else:
        print("No solution")

#iterative A*
def caso_prueba5(mov):
    heuristics = Heuristics.bloques_correctos
    cubo = Cube()
    imprimir_cubo(cubo.cubo)
    print(shuffle_cube(cubo, mov))
    print('After movements:')
    imprimir_cubo(cubo.cubo)
    solver = Solver(cubo)
    path = solver.iterative_deepening_A_star(heuristics)
    if path:
        print(path)
        return len(path)
    else:
        print("No solution")
        return 0


times = []
for _ in range(21):
    start_time = time.time()
    caso_prueba3(3)
    execution_time = time.time() - start_time
    print(execution_time)
    times.append(execution_time)
print(times)

