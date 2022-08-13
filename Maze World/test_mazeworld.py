from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)


# Your additional tests here:

# 5x5
test_maze6 = Maze("maze6.maz")
test_mp = MazeworldProblem(test_maze6, (3, 1))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)
#
# # 8x8
# test_maze8 = Maze("maze8.maz")
# test_mp = MazeworldProblem(test_maze8, (7, 0))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)
#
# # 10x10
# test_maze7 = Maze("maze7.maz")
# test_mp = MazeworldProblem(test_maze7, (7, 8))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)
#
# # 20x20
# test_maze5 = Maze("maze5.maz")
# test_mp = MazeworldProblem(test_maze5, (18, 1, 1, 5, 1, 1))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)
#
# # 40x40
# # test_maze4 = Maze("maze4.maz")
# # test_mp = MazeworldProblem(test_maze4, (38, 38, 37, 38, 38, 37))
# # result = astar_search(test_mp, test_mp.manhattan_heuristic)
# # print(result)
# # test_mp.animate_path(result.path)