
class BFS(object):
    def __init__(self, board, logic):
        self.board = board
        self.logic = logic

    def run_search(self):
        open_list = []
        closed_list = set()
        initial_state = self.logic.get_initial_state()

        open_list.append(initial_state)

        while len(open_list):
            current_node = open_list.pop(0)
            closed_list.add(current_node)
            if self.logic.goal_state_check(current_node):
                return self.logic.cycle_back()
            sons = self.logic.next_states(current_node)
            for son in sons:
                if son not in closed_list:
                    open_list.append(son)

        raise Exception("Puzzle can not be solved.")

