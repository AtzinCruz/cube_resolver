#Basic Nodes
class Node:
    def __init__(self, cube):
        self.cube = cube
        self.path = []

#Nodes with heuristic value

class Nodeh:
    def __init__(self, cube):
        self.cube = cube
        self.value_heuristic = -1
        self.path = []
        
    def calculate_heuristic(self, heuristic):
        self.value_heuristic = heuristic(self.cube)

    
    def __lt__(self, other):
        return self.value_heuristic < other.value_heuristic


    
class NodeAStar(Nodeh):
    def __init__(self, cube):
        super().__init__(cube)
        self.distance = 0

    def __lt__(self, other):
        return self.value_heuristic + self.distance < other.value_heuristic + other.distance  
    
    def __eq__(self, other):
        return isinstance(other, NodeAStar) and self.cube == other.cube
    
    def __hash__(self) -> int:
        cube_tuple = tuple(map(lambda x: tuple(map(tuple, x)), self.cube))
        return hash(cube_tuple)
    
    