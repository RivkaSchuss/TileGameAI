class GameLogic(object):

    def __init__(self, board, board_size):
        self.board = board
        self.board_size = board_size

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

    def get_next_moves(self):
        result = []
        pos = self.get_location()
        board = self.board
        move_up = board[0] - 1, board[1]
        move_down = board[0] + 1, board[1]
        move_right = board[0], board[1] + 1
        move_left = board[0], board[1] - 1

        #up
        #if

        #down

        #right

        #left
        return result

    def construct_path(self, state, path_formed):
        action_list = list()

        while path_formed[state][0] is not None:
            state, action = path_formed[state]
            action_list.append(action)
        action_list.reverse()
        return action_list

    def get_location(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == '0':
                    return row, col
        return -1, -1

    def swap(self, location, value):
        loc_i, loc_j = location[0], location[1]
        val_i, val_j = value[0], value[1]
        self.board[loc_i][loc_j], self.board[val_i][val_j] = self.board[loc_i][loc_j], self.board[val_i][val_j]
