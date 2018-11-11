import Queue


class BFS(object):
    def __init__(self, board, logic):
        self.board = board
        self.logic = logic

    def run_search(self):
        open_list = Queue.Queue()
        closed_list = set()
        path_formed = dict()
        initial_state = self.logic.get_initial_state()

        open_list.put(initial_state)
        path_formed[initial_state] = (None, None)

        while not open_list.empty():
            current_node = open_list.get()
            closed_list.add(current_node)

            if self.logic.goal_state_check(current_node):
                return self.logic.construct_path(current_node, path_formed), str(len(closed_list)), '0'

            children = self.logic.get_next_moves(current_node)
            for (child, action) in children:
                if child in closed_list:
                    continue
                if child not in open_list:
                    path_formed[child] = (current_node, action)
                    open_list.put(child)

        raise Exception("Puzzle can not be solved.")

