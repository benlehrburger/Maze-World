from Maze import Maze
from time import sleep

# wrap a sensorless problem object
class SensorlessProblem:

    def __init__(self, maze):
        # initialize our start state tuple
        start_state = ()
        # add each coordinate pair in the maze that is not a wall
        for col in range(0, maze.width):
            for row in range(0, maze.height):
                if maze.is_floor(col, row):
                    start_state = start_state + (col,) + (row,)

        self.start_state = start_state
        self.maze = maze

    # get successors method gets a successor in each cardinal direction
    def get_successors(self, state):
        # move each coordinate one unit north
        north_successors = self.directional_state(state, 1, 1)
        # move each coordinate one unit south
        south_successors = self.directional_state(state, 1, -1)
        # move each coordinate one unit east
        east_successors = self.directional_state(state, 0, 1)
        # move each coordinate one unit west
        west_successors = self.directional_state(state, 0, -1)

        # return all directional states
        return [north_successors, south_successors, east_successors, west_successors]

    # helper method to get successors efficiently
    def directional_state(self, state, coordinate, direction):
        # initialize empty state, counting index, and coordinate set so we don't repeat coordinates
        new_state, idx, added_set = (), 0, set()

        # while there are still coordinates in our state
        while idx < len(state) - 1:
            # make the current coordinate pair mutable
            coordinate_pair = [state[idx], state[idx + 1]]
            # increment/decrement each coordinate in its specified direction
            coordinate_pair[coordinate] += direction

            # if the new coordinate is a floor space
            if self.maze.is_floor(coordinate_pair[0], coordinate_pair[1]):
                # and if we haven't already added it to our new state
                if tuple(coordinate_pair) not in added_set:
                    # add the new coordinates to our state
                    new_state += tuple(coordinate_pair)
                    # add the new coordinates to our set
                    added_set.add(tuple(coordinate_pair))
            # otherwise, we hit a wall and the robot didn't move
            else:
                # so if the existing coordinate isn't in our new state already
                if (state[idx], state[idx + 1]) not in added_set:
                    # add the existing coordinates to our state
                    new_state += (state[idx], state[idx + 1])
                    # add the existing coordinates to our set
                    added_set.add((state[idx], state[idx + 1]))
            idx += 2

        return new_state

    # method to check if we've reached our goal state
    def goal_reached(self, state):
        # our goal state is achieved when the robot knows where it is
        if len(state) == 2:
            return True

        return False

    # derive our heuristic for the sensorless robot
    def sensorless_heuristic(self, state):
        # heuristic is optimistic when it is never greater than n
        return len(state) / 2 - 1

    # method to check if a child node holds the same state as its parent
    # returns True if they share the same state, in which case we don't want to add both
    def same_state(self, node_state, child_state):
        if node_state == child_state:
            return True

        return False

    # method to update the robot's current location based on the new state
    def update_robotloc(self, state):
        self.maze.robotloc = state

    def __str__(self):
        string =  "Blind robot problem: "
        return string


    # given a sequence of states (including robot turn), modify the maze and print it out
    # be careful, this does modify the maze
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))


# a bit of test code
if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
    print(test_problem.get_successors(test_problem.start_state))
