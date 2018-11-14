class BFS(object):
    def __init__(self, state, logic):
        self.state = state
        self.logic = logic

    """
    running the BFS search algorithm
    """
    def run_search(self):
        open_list = []
        closed_list = list()
        initial_state = self.logic.get_initial_state()

        # adding the initial state to the open list
        open_list.append(initial_state)

        while len(open_list):

            current_node = open_list.pop(0)
            closed_list.append(current_node)

            # if we've arrived at the goal state
            if self.logic.goal_state_check(current_node):
                path = "".join(self.logic.construct_path(current_node))
                return path, str(len(closed_list)), '0'

            # defining the current node's successors
            children = self.logic.get_next_moves(current_node)

            # iterating over the successors
            for child in children:
                if child in closed_list:
                    continue
                if child not in open_list:
                    # path_formed[child] = current_node
                    open_list.append(child)

        raise Exception("Puzzle can not be solved.")

