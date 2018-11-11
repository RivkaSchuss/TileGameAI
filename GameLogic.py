class GameLogic(object):

    def __init__(self, board, board_size):
        self.board = board

    def get_initial_state(self):
        result = []
        return result

    def goal_state_check(self):
        count = 1
        for row in self.board:
            for node in row:
                if node != '0' and node != str(count):
                    return False
                count += 1
        return True

    def get_next_move(self):
        result = []
        return result

    def cycle_back(self, goal):
        path = []
        current = goal
