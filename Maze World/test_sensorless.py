from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search

# initialize maze object
test_maze3 = Maze("maze3.maz")
# wrap the maze object in a sensorless problem object
test_sp = SensorlessProblem(test_maze3)

# capture the result of A* searching with a sensorless robot
result = astar_search(test_sp, test_sp.sensorless_heuristic)
print(result)
test_sp.animate_path(result.path)

# initialize maze object
test_maze7 = Maze("maze7.maz")
# wrap the maze object in a sensorless problem object
test_sp = SensorlessProblem(test_maze7)

# capture the result of A* searching with a sensorless robot
result = astar_search(test_sp, test_sp.sensorless_heuristic)
print(result)
test_sp.animate_path(result.path)
