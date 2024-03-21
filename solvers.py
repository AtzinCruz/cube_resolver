from collections import deque
import copy
from nodes import Nodeh, Node
import heapq

class Solver:
    def __init__(self, cube):
        self.cube = cube

    
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
    
    #BFS with heuristcs
    def bfs_h(self, heuristic):
        cube = self.cube
        start_node = Nodeh(copy.deepcopy(cube.cubo))
        goal_node = Node(copy.deepcopy(cube.cubo_resuelto))
        visited = set()
        priority_queue = []
        heapq.heappush(priority_queue, (start_node.value_heuristic, start_node))

        while priority_queue:
            current_node = heapq.heappop(priority_queue)[1]
            if current_node.cube == goal_node.cube:
                return True, current_node.path
            
            visited.add(current_node)
            
            for move in cube.movements.keys():
                new_cube_state = copy.deepcopy(current_node.cube)
                cube.cubo = new_cube_state
                cube.move(move)
                neighbor_node = Nodeh(cube.cubo)
                neighbor_node.path = current_node.path + [move]
                neighbor_node.calculate_heuristic(heuristic)

                if neighbor_node not in visited:
                    heapq.heappush(priority_queue, (neighbor_node.value_heuristic, neighbor_node))
                    visited.add(neighbor_node)
        return False
