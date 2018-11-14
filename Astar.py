from heapq import heappush, heappop


class Astar(object):
    def __init__(self, state, logic):
        self.state = state
        self.logic = logic

    def run_search(self):
        open_list = []
        closed_list = set()
        initial_state = self.logic.get_initial_state()
        initial_state.depth = 0
        initial_state.heuristic = self.calculate_trip_cost(initial_state)
        heappush(open_list, (initial_state.get_f, initial_state))

        while open_list:
            current_node = heappop(open_list)[1]

            if self.logic.goal_state_check(current_node):
                path = "".join(self.logic.construct_path(current_node))
                return path, str(len(closed_list)), len(path)

            if current_node in closed_list:
                continue

            children = self.logic.get_next_moves(current_node)
            for child in children:
                child.depth = current_node.depth + 1
                child.heuristic = self.calculate_trip_cost(child)
                heappush(open_list, (child.get_f, child))

            closed_list.add(current_node)
            print len(closed_list)

        raise Exception("Puzzle can not be solved.")

    def calculate_trip_cost(self, state):
        cost = 0
        board = state.board
        for r, row in enumerate(board):
            for c, num in enumerate(row):
                num = int(num)
                if num != 0:
                    correct_r, correct_c = int((num - 1) / self.logic.board_size), (num - 1) % self.logic.board_size
                    cost += abs(correct_r - r) + abs(correct_c - c)
        return cost

    def get_f(self, state):
        return state.depth + state.heuristic

