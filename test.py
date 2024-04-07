from nodes import NodeAStar
from cube import Cube
node = NodeAStar(Cube().cubo_resuelto)
print(hash(node))
node2 = NodeAStar(Cube().cubo_resuelto)
print(hash(node))