from GameLogic import GameLogic


class IDS(object):
    def __init__(self, board, logic):
        self.board = board
        self.logic = logic

    def run_search(self):
        result = "ids has been chosen"
        initial_state = self.logic.get_initial_state()
        return result


