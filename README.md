# Rubik's Cube Solver

This Python program provides functionality to solve a Rubik's Cube using various search algorithms and heuristics.

## Description

The Rubik's Cube Solver consists of multiple Python classes that represent the Rubik's Cube itself, as well as different algorithms and heuristics to solve it.

- `Cube`: Represents the Rubik's Cube and provides methods to manipulate it, such as rotating faces and performing moves.
- `Solver`: Contains implementations of various search algorithms to solve the Rubik's Cube, including Breadth First Search (BFS), A* Search, and Iterative Deepening A* (IDA*).
- `Heuristics`: Defines different heuristic functions used to estimate the cost of reaching the goal state, such as the Manhattan distance and the number of correctly positioned blocks or corners.

## Necessary libraries
from cube import Cube
from solver import Solver
from heuristics import Heuristics


## Usage

1. Clone the repository:

```bash
git clone https://github.com/AtzinCruz/rubiks-cube-solver.git


