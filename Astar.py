
class Astar(object):
    def __init__(self, state, logic):
        self.state = state
        self.logic = logic

    def run_search(self):
        result = []
        open_list = []
        closed_list = []
        initial_state = self.logic.get_initial_state()
        open_list.append(initial_state)

        while len(open_list):
            current_node = open_list.pop(0)
            current_node.depth += 1
            closed_list.append(current_node)

            if self.logic.goal_state_check(current_node):
                cost = self.calculate_trip_cost(current_node)
                path = "".join(self.logic.construct_path(current_node))
                return path, str(len(closed_list)), str(cost)

            children = self.logic.get_next_moves(current_node)
            for child in children:
                open_list.append(child)

        return result

    def calculate_trip_cost(self, state):
        cost = 0
        while state is not None:
            cost += self.get_f(state)
            state = state.previous
        return cost

    def get_f(self, state):
        return state.depth + self.get_heuristic_sum(state)

    def get_heuristic_sum(self, state):
        heuristic_sum = 0
        board_size = self.logic.board_size
        for i in range(board_size):
            for j in range(board_size):
                heuristic_sum += self.heuristic_func(state.board[i][j], i, j)

        return heuristic_sum

    def heuristic_func(self, tile, row, col):
        board_size = self.logic.board_size
        if tile == 0:
            return abs(row - board_size - 1) + abs(col - board_size - 1)

        moved_row = int(round(int(tile)/board_size) - 1)
        moved_col = (int(tile) % board_size + (board_size - 1)) % board_size
        return abs(row - moved_row) + abs(col - moved_col)



