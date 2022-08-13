from Maze import Maze
from time import sleep

# wrap a mazeworld problem object
class MazeworldProblem:

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations

        # if we get a start state without a robot to move
        if len(maze.robotloc) % 2 == 0:
            mutable_location = list(maze.robotloc)
            # have the program move the 0th robot first
            mutable_location.insert(0,0)
            self.start_state = tuple(mutable_location)
        else:
            # otherwise our start state is the current locations of the robots
            self.start_state = maze.robotloc


    def __str__(self):
        string =  "Mazeworld problem: "
        return string

    # method to update the robot's current location
    def update_robotloc(self, state):
        mutable_state = list(state)
        self.maze.robotloc = mutable_state[1:]

    # method to check if a node and its child have the same state
    # returns True if they share the same state, in which case we don't want to add both
    def same_state(self, node_state, child_state):
        if node_state[1:] == child_state[1:]:
            return True

        return False

    # method to define calculation of the Manhattan heuristic
    def manhattan_heuristic(self, state):
        # get locations of the robots
        bots = self.parse_locations(state)
        # get goal locations for those robots
        goals = self.parse_locations(self.goal_locations)

        heuristic = 0
        for bot_loc in bots:
            goal_loc = goals[bots.index(bot_loc)]
            # Sum the differences between robots' current locations and their goal locations
            x = abs(bot_loc[0] - goal_loc[0])
            y = abs(bot_loc[1] - goal_loc[1])
            heuristic += x
            heuristic += y

        return heuristic

    # helper method to parse and isolate a tuple of robot locations into its individual coordinate pairs
    def parse_locations(self, locations):
        locations = list(locations)

        # if the list is not even in length, that means we have to get rid of the robot-move indicator
        if len(locations) % 2 != 0:
            del locations[0]
        coordinate_pairs, idx = [], 0

        # before we run out of coordinate pairs
        while idx < len(locations) - 1:
            # retrieve the x-y coordinates for that pair and add it to our mutable list
            x_y = [locations[idx], locations[idx + 1]]
            coordinate_pairs.append(x_y)
            idx += 2

        return coordinate_pairs

    # get children of the current node
    def get_successors(self, state):
        # retrieve the robot we want to find children for and use it to index
        print(state)
        robot_to_move = state[0]
        location_index = 2 * robot_to_move
        robot_location = self.maze.robotloc[location_index:location_index + 2]

        # move one unit north
        north = (robot_location[0], robot_location[1] + 1)
        # move one unit south
        south = (robot_location[0], robot_location[1] - 1)
        # move one unit east
        east = (robot_location[0] + 1, robot_location[1])
        # move one unit west
        west = (robot_location[0] - 1, robot_location[1])
        states = [north, south, east, west]

        # add the robot's current position as a successor of itself
        successors = [tuple(robot_location)]

        # for each cardinal direction
        for direction in states:
            # add the robot as a valid successor if it is moving to a floor square without a robot on it
            if self.maze.is_floor(direction[0], direction[1]) and not self.maze.has_robot(direction[0], direction[1]):
                successors.append(direction)

        # convert each successor into a tuple
        successor_tuples = []
        for child in successors:
            mutable_state = list(state)
            mutable_state[0] = int((robot_to_move + 1) % (len(self.goal_locations) / 2))
            mutable_state[location_index + 1] = child[0]
            mutable_state[location_index + 2] = child[1]
            successor_tuples.append(tuple(mutable_state))

        return successor_tuples

    # check if we have reached our goal state
    def goal_reached(self, state):
        # remove the robot to move from our state
        mutable_state = list(state)
        del mutable_state[0]

        # return true if the current state is our goal state
        if tuple(mutable_state) == self.goal_locations:
            return True

        return False

    # given a sequence of states (including robot turn), modify the maze and print it out
    # be careful, this does modify the maze
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


# a bit of test code
if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
