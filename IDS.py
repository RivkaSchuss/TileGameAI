from copy import deepcopy


class IDS(object):
    def __init__(self, state, logic):
        self.state = state
        self.logic = logic
        self.checked = 1

    """
    runs the IDS search algorithm
    """
    def run_search(self):
        result = None
        limit = 1

        # if we haven't achieved a result yet
        while not result:
            self.checked = 0
            result = self.limited_DFS(self.state, 0, limit)
            limit += 1

        return result

    def limited_DFS(self, initial_state, iteration=0, limit=0):

        # copying the current node
        current_node = deepcopy(initial_state)

        # raising the counter of the nodes that have been checked
        self.checked += 1

        # if we've arrived at the goal state
        if self.logic.goal_state_check(current_node):
            path = "".join(self.logic.construct_path(current_node))
            return path, self.checked, str(iteration)

        # if the number of iterations performed is equal to the limit, stop the iteration
        if iteration == limit:
            return None

        # defining the current node's successors
        children = self.logic.get_next_moves(current_node)

        # iterating over the successors
        for child in children:

            # run the algorithm again recursively
            result = self.limited_DFS(child, iteration + 1, limit)

            # if we've acquired a result
            if result is not None:
                return result

        return None






