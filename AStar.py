from math import sqrt
from queue import PriorityQueue
class Node:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.heuristic_value = -1
        self.path = []

    def calculate_heuristic(self, other, heuristic):
        self.heuristic_value = heuristic(self, other)

    

class NodeAStar(Node):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
        self.distance = 0
        

    def __lt__(self, other: any) -> bool:
        if not isinstance(other, NodeAStar):
            return False

        return self.distance + self.heuristic_value < other.distance + other.heuristic_value

    def __gt__(self, other: any) -> bool:
        if not isinstance(other, NodeAStar):
            return False
        return self.distance + self.heuristic_value > other.distance + other.heuristic_value

    def __eq__(self, other: any) -> bool:
        if not isinstance(other, NodeAStar):
            return False
        return self.row == other.row and self.col == other.col

class Heuristics:
    @staticmethod
    def manhattan_distance(node_a: NodeAStar, node_b: NodeAStar) -> float:
        return abs(node_a.row - node_b.row) + abs(node_a.col - node_b.col)

    @staticmethod
    def eucliudean_distance(node_a: NodeAStar, node_b: NodeAStar) -> float:
        return sqrt((node_a.col - node_b.col) ** 2 + (node_a.row - node_b.row) ** 2)

    

class World:
    def __init__(self, world : list[list]) -> None:
        self.world = world
        self.rows = len(world)
        self.cols = len(world[0])
        self.movement_4 =[[-1, 0],
                          [0, 1],
                          [1, 0],
                          [0, -1]]
        self.movement_8 =[[-1, 0], [0, 1],
                          [1, 0], [0, -1],
                          [-1, -1], [-1, 1], 
                          [1, -1], [1, 1]]


    def a_star_8_M(self, srow, scol, trow, tcol, heuristic):
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        pq = PriorityQueue()

        source = NodeAStar(srow, scol)
        source.path.append((source.row, source.col))
        target = NodeAStar(trow, tcol)

        pq.put(source)

        while not pq.empty():
            current_node : NodeAStar = pq.get()
            if current_node == target:
                print("Path Found")
                print(current_node.path)
                return None
            if self.visited[current_node.row][current_node.col]:
                continue

            self.visited[current_node.row][current_node.col] = True
            for i, j in self.movement_8:
                next_col = current_node.col + i
                next_row = current_node.row + j
                if 0 <= next_col < self.cols and 0 <= next_row < self.rows and not self.visited[next_row][next_col] and self.world[next_row][next_col]!= "x":
                    next_node = NodeAStar(next_row, next_col)
                    next_node.calculate_heuristic(target, heuristic)
                    next_node.distance = current_node.distance + 1
                    next_node.path = current_node.path + [(next_node.row, next_col)]
                    pq.put(next_node)
        print("Unable to find path")

    def a_star_4_M(self, srow, scol, trow, tcol, heuristic):
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        pq = PriorityQueue()

        source = NodeAStar(srow, scol)
        source.path.append((source.row, source.col))
        target = NodeAStar(trow, tcol)

        pq.put(source)

        while not pq.empty():
            current_node : NodeAStar = pq.get()
            if current_node == target:
                print("Path Found")
                print(current_node.path)
                return None
            if self.visited[current_node.row][current_node.col]:
                continue

            self.visited[current_node.row][current_node.col] = True
            for i, j in self.movement_4:
                next_col = current_node.col + i
                next_row = current_node.row + j
                if 0 <= next_col < self.cols and 0 <= next_row < self.rows and not self.visited[next_row][next_col] and self.world[next_row][next_col]!= "x":
                    next_node = NodeAStar(next_row, next_col)
                    next_node.calculate_heuristic(target, heuristic)
                    next_node.distance = current_node.distance + 1
                    next_node.path = current_node.path + [(next_node.row, next_col)]
                    pq.put(next_node)
        print("Unable to find path")
        

map = [['.', '.', '.', '.'],
       ['.', '.', 'x', '.'],
       ['.', '.', 'x', '.'],
       ['.', '.', 'x', '.']]
       

world = World(map)
world.a_star_4_M(0, 0, 3, 3, Heuristics.manhattan_distance)
world.a_star_8_M(0, 0, 3, 3, Heuristics.eucliudean_distance)