from copy import deepcopy


class IDS(object):
    def __init__(self, state, logic):
        self.state = state
        self.logic = logic
        self.checked = 1

    def run_search(self):
        result = None
        limit = 1

        while not result:
            self.checked = 0
            result = self.limited_DFS(self.state, 0, limit)
            limit += 1

        return result

    def limited_DFS(self, initial_state, iteration=0, limit=0):
        current_node = deepcopy(initial_state)
        self.checked += 1
        print self.checked

        if self.logic.goal_state_check(current_node):
            path = "".join(self.logic.construct_path(current_node))
            return path, self.checked, str(iteration)

        if iteration == limit:
            return None

        children = self.logic.get_next_moves(current_node)
        for child in children:
            result = self.limited_DFS(child, iteration + 1, limit)
            if result is not None:
                return result

        return None






