import random
from cube import Cube
from solvers import Solver
from heuristics import Heuristics

# Print cube in matrix form
def imprimir_cubo(cubo):
    for lado in cubo:
        for fila in lado:
            print(fila)
        print()

# Shuffle cube manually
def shuffle_manually(cubo):
    movimientos_manuales = ['U', 'u', 'D', 'd', 'L', 'l', 'R', 'r', 'F', 'f', 'B', 'b']
    while True:
        movimiento = input("Ingresa un movimiento ('U', 'u', 'D', 'd', 'L', 'l', 'R', 'r', 'F', 'f', 'B', 'b') o 'q' para terminar: ")
        if movimiento == 'q':
            break
        elif movimiento in movimientos_manuales:
            cubo.move_manual(movimiento)
            imprimir_cubo(cubo.cubo)
        else:
            print("Movimiento no válido. Inténtalo de nuevo.")
    return cubo

# Random shuffle
def shuffle_random(cube, num_moves=20):
    moves = []
    valid_moves = cube.movements.keys()
    for _ in range(num_moves):
        move = random.choice(list(valid_moves))
        cube.move(move)
        moves.append(move)
    return moves

# Menu principal
def main_menu():
    cubo = Cube()
    while True:
        print("1. Revolver manualmente")
        print("2. Revolver aleatoriamente")
        print("3. Resolver cubo")
        choice = input("Elige una opción: ")
        if choice == '1':
            imprimir_cubo(cubo.cubo)
            cubo = shuffle_manually(cubo)
        elif choice == '2':
            num_moves = int(input("Ingresa el número de movimientos para revolver aleatoriamente el cubo: "))
            print(shuffle_random(cubo, num_moves))
            print('After movements:')
            imprimir_cubo(cubo.cubo)
        elif choice == '3':
            select_solver(cubo)
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            main_menu()

# Selección de solucionador y heurística
def select_solver(cubo):
    print("Selecciona un método de resolución:")
    print("1. BFS")
    print("2. BFS con heurística")
    print("3. A*")
    print("4. Búsqueda iterativa A*")
    method = input("Elige una opción: ")
    if method == '1':
        solver = Solver(cubo)
        flag, path = solver.bfs()
        print_solution(flag, path)
    elif method == '2':
        select_heuristic(cubo)
    elif method == '3':
        select_heuristic(cubo, use_a_star=True)
    elif method == '4':
        select_heuristic(cubo, use_a_star=True, iterative=True)
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        select_solver(cubo)

# Selección de heurística
def select_heuristic(cubo, use_a_star, iterative=False):
    print("Selecciona una heurística:")
    print("1. Bloques correctos")
    print("2. Capas resueltas")
    choice = input("Elige una opción: ")
    if choice == '1':
        heuristic = Heuristics.bloques_correctos
    elif choice == '2':
        heuristic = Heuristics.capas_resueltas
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        select_heuristic(cubo, use_a_star, iterative)

    solver = Solver(cubo)
    if use_a_star:
        if iterative:
            path = solver.iterative_deepening_A_star(heuristic)
        else:
            path = solver.A_star(heuristic)
    else:
        flag, path = solver.bfs_h(heuristic)

    print_solution(flag if not use_a_star else path is not None, path)

# Imprimir solución
def print_solution(flag, path):
    if flag:
        print("Solución encontrada:")
        print(path)
    else:
        print("No se ha encontrado solución.")

if __name__ == "__main__":
    main_menu()
