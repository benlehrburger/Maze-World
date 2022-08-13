from SearchSolution import SearchSolution
from heapq import heappush, heappop

# wrap an A* search node object
class AstarNode:

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    # A* priority = g(n) + h(n)
    def priority(self):
        return self.transition_cost + self.heuristic

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back as far as possible
# grab the states from the nodes and reverse the resulting list of states
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result

# function to execute A* search
def astar_search(search_problem, heuristic_fn):
    # starter code

    # initialize root node object
    node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    # initialize frontier heap
    frontier = []
    heappush(frontier, node)

    # initialize solution object
    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    # initialize dictionary to hold a node's state and its associated transition cost
    visited_cost = {}
    visited_cost[node.state] = 0

    # current transition cost equals the current node's transition cost
    transition_cost = node.transition_cost

    # until we reach our goal state
    while not search_problem.goal_reached(node.state):

        # if the frontier heap is empty then we haven't found a solution
        if not frontier:
            return 'failure'

        # pop the highest priority node from the heap
        node = heappop(frontier)
        # increment the number of nodes visited in the solution object
        solution.nodes_visited += 1

        # if we have reached our goal state
        if search_problem.goal_reached(node.state):
            # backchain from our current node back to the root
            solution.path = backchain(node)
            # update the final cost to hold the current transition cost
            solution.cost = node.transition_cost
            # return the solution object
            return solution

        # update the robot's current location to the node's current state
        search_problem.update_robotloc(node.state)
        # add the current node and its transition cost to the dictionary
        visited_cost[node.state] = transition_cost

        # for each successor of the current node
        for successor in search_problem.get_successors(node.state):

            # if the node's child is in a different position
            if not search_problem.same_state(node.state, successor):
                # then make it a node object and increment its transition cost
                child = AstarNode(successor, heuristic_fn(successor), node, node.transition_cost + 1)
            else:
                # otherwise make it a node object without incrementing its transition cost
                child = AstarNode(successor, heuristic_fn(successor), node, node.transition_cost)

            # if the current child hasn't been visited yet
            if child.state not in visited_cost:
                # add it to the frontier heap
                heappush(frontier, child)
            # otherwise, if the current child has been visited and has a lower cost than when we last visited it
            elif child.state in visited_cost and child.transition_cost < visited_cost.get(child.state):
                # replace the higher cost node with the lower cost node
                heappush(frontier, child)
