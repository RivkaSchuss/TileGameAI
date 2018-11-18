from heapq import heappush, heappop


class Astar(object):
    def __init__(self, state, logic):
        self.state = state
        self.logic = logic

    """
    runs the a* search algorithm
    """
    def run_search(self):
        open_list = []
        counter = 0
        # defining the initial state's depth and heuristic value
        initial_state = self.logic.get_initial_state()
        initial_state.depth = 0
        initial_state.heuristic = self.calculate_trip_cost(initial_state)

        # adding the initial state into the open list heap, and calculating its f
        heappush(open_list, (initial_state.get_f, initial_state))

        while open_list:
            current_node = heappop(open_list)[1]

            # if we've arrived at the goal state
            if self.logic.goal_state_check(current_node):
                path = "".join(self.logic.construct_path(current_node))
                return path, str(counter), len(path)

            # defining the current node's successors
            children = self.logic.get_next_moves(current_node)

            # comparing the successors
            for child in children:
                child.depth = current_node.depth + 1
                child.heuristic = self.calculate_trip_cost(child)
                heappush(open_list, (child.get_f, child))

            # raising the counter of the nodes that have been checked
            counter += 1

        raise Exception("Puzzle can not be solved.")

    """
    runs the manhattan distance heuristic function
    """
    def calculate_trip_cost(self, state):
        cost = 0
        board = state.board
        # iterating over the game board
        for r, row in enumerate(board):
            for c, num in enumerate(row):
                num = int(num)
                if num != 0:
                    # calculating the correct index for the current tile
                    correct_r, correct_c = int((num - 1) / self.logic.board_size), (num - 1) % self.logic.board_size
                    # calculating the cost to place the correct tile in its place
                    cost += abs(correct_r - r) + abs(correct_c - c)
        return cost


