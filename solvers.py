from collections import deque
import copy
from nodes import Nodeh, Node, NodeAStar
from queue import PriorityQueue
from cube import Cube

class Solver:

    INF = float("inf")

    def __init__(self, cube : Cube):
        self.cube = cube
        self.path = []
    
    #BFS without heuristic
    def bfs(self):
        cube = self.cube
        start_node = Node(copy.deepcopy(cube.cubo))
        goal_node = Node(copy.deepcopy(cube.cubo_resuelto))
        visited = set()
        queue = deque([start_node])

        while queue:
            current_node = queue.popleft()
            if current_node.cube == goal_node.cube:
                return True, current_node.path

            visited.add(current_node)

            for move in cube.movements.keys():
                new_cube_state = copy.deepcopy(current_node.cube)
                cube.cubo = new_cube_state
                cube.move(move)
                neighbor_node = Node(cube.cubo)
                neighbor_node.path = current_node.path + [move]

                if neighbor_node not in visited:
                    queue.append(neighbor_node)
                    visited.add(neighbor_node)

        return False
    

    def bfs_h(self, heuristic):
        start_node = Nodeh(copy.deepcopy(self.cube.cubo))
        target_node_configuration = copy.deepcopy(self.cube.cubo_resuelto)
        pq = PriorityQueue()
        visited = set()
        pq.put(start_node)

        while not pq.empty():
            current_cube : Nodeh = pq.get()
            if current_cube.cube == target_node_configuration:
                return True, current_cube.path
            
            if current_cube in visited:
                continue

            visited.add(current_cube)
            for move in self.cube.movements.keys():
                next_cube = copy.deepcopy(current_cube.cube)
                self.cube.cubo = next_cube
                self.cube.move(move)
                neighbor_node = Nodeh(self.cube.cubo)  
                neighbor_node.path = current_cube.path + [move]
                neighbor_node.calculate_heuristic(heuristic)
                pq.put(neighbor_node)

        return False, None


    #A star
    def A_star(self, heuristic):
        start_node = NodeAStar(copy.deepcopy(self.cube.cubo))
        target_node_configuration = copy.deepcopy(self.cube.cubo_resuelto)
        pq = PriorityQueue()
        visited = set()
        pq.put(start_node)

        while not pq.empty():
            current_cube : NodeAStar = pq.get()
            if current_cube.cube == target_node_configuration:
                return current_cube.path
            
            if current_cube in visited:
                continue

            visited.add(current_cube)
            for move in self.cube.movements.keys():
                next_cube = copy.deepcopy(current_cube.cube)
                self.cube.cubo = next_cube
                self.cube.move(move)
                neighbor_node = NodeAStar(self.cube.cubo)  
                neighbor_node.path = current_cube.path + [move]
                neighbor_node.calculate_heuristic(heuristic)
                neighbor_node.distance = current_cube.distance + 1
                pq.put(neighbor_node)

        return None
    
    #IDAStar
    def iterative_deepening_A_star(self, heuristic):
        start_node = NodeAStar(copy.deepcopy(self.cube.cubo))
        end_configuration = self.cube.cubo_resuelto
        start_node.calculate_heuristic(heuristic)
        bound = start_node.distance
        path = [start_node]
        while True:
            t = self.__search(path, bound, heuristic, end_configuration)
            if t == True:
                return self.path
            if t == Solver.INF:
                return None
            bound = t

            
    def __search(self, path, bound, heuristic, end_configuration):
        path_f = path
        node: NodeAStar = path_f[-1]
        f = node.distance + node.value_heuristic
        if f > bound:
            return f
        if node.cube == end_configuration:
            self.path = node.path
            return True
        min = Solver.INF
        for succ in self.__sucessors(node, heuristic):
            if succ not in path:
                path_f.append(succ)
                t = self.__search(path, bound, heuristic, end_configuration)
                if t == True:
                    return True
                if t < min:
                    min = t
                path.pop()
        return min
        
    def __sucessors(self, state, heuristic):
        current_state = state
        next_states = []
        for move in self.cube.movements.keys():
            next_cube = copy.deepcopy(current_state.cube)
            self.cube.cubo = next_cube
            self.cube.move(move)
            neighbor_node = NodeAStar(self.cube.cubo)  
            neighbor_node.path = current_state.path + [move]
            neighbor_node.calculate_heuristic(heuristic)
            neighbor_node.distance = current_state.distance + 1
            next_states.append(neighbor_node)
        return next_states