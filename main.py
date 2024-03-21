import random
from cube import Cube
from solvers import Solver
from heuristics import Heuristics

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

def shuffle_cube(cube, num_moves=20):
    moves = []
    valid_moves = cube.movements.keys()
    for _ in range(num_moves):
        move = random.choice(list(valid_moves))
        cube.move(move)
        moves += move
    return moves

def caso_prueba1():
    cubo = Cube()
    imprimir_cubo(cubo.cubo)
    cubo.move_manual('B')
    cubo.move_manual('b')
    print('After movements:')
    imprimir_cubo(cubo.cubo)

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

def caso_prueba3(mov):
    heuristic = Heuristics.capas_resueltas
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

caso_prueba2(3)