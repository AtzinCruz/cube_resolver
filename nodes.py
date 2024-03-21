class Node:
    def __init__(self, cube):
        self.cube = cube
        self.path = []

class Nodeh:
    def __init__(self, cube):
        self.cube = cube
        self.value_heuristic = -1
        self.path = []
        
    def calculate_heuristic(self, heuristic):
        self.value_heuristic = heuristic(self.cube)

    
    def __lt__(self, other):
        return self.value_heuristic < other.value_heuristic