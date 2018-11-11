from GameLogic import GameLogic


class Astar(object):
    def __init__(self, board, logic):
        self.board = board
        self.logic = logic

    def run_search(self):
        result = "a* has been chosen"
        initial_state = self.logic.get_initial_state()
        return result

