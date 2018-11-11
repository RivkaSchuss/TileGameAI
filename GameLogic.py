class GameLogic(object):

    def __init__(self, state, board_size):
        self.state = state
        self.board_size = board_size

    def get_initial_state(self):
        return self.state

    def goal_state_check(self, state):
        count = 1
        for row in state.board:
            for node in row:
                if node != '0' and node != str(count):
                    return False
                count += 1
        return True

    def get_next_moves(self, state):
        result = list()
        empty_space = self.get_empty_space(self.state)
        move_up = empty_space[0] - 1, empty_space[1]
        move_down = empty_space[0] + 1, empty_space[1]
        move_right = empty_space[0], empty_space[1] + 1
        move_left = empty_space[0], empty_space[1] - 1
        #up
        if self.check_valid(move_up):
            copied = state.copy()
            self.swap(empty_space, move_up, copied)
            state_to_add = State(copied, 'U')
            result.append(state_to_add)
        #down
        if self.check_valid(move_down):
            copied = state.copy()
            self.swap(empty_space, move_down, copied)
            state_to_add = State(copied, 'D')
            result.append(state_to_add)
        #left
        if self.check_valid(move_left):
            copied = state.copy()
            self.swap(empty_space, move_left, copied)
            state_to_add = State(copied, 'L')
            result.append(state_to_add)
        # right
        if self.check_valid(move_right):
            copied = state.copy()
            self.swap(empty_space, move_right, copied)
            state_to_add = State(copied, 'R')
            result.append(state_to_add)
        return result

    def construct_path(self, state, path_formed):
        action_list = list()

        while path_formed[state][0] is not None:
            state, action = path_formed[state]
            action_list.append(state.move)

        action_list.reverse()
        return action_list

    def check_valid(self, position):
        return 0 <= position[0] < self.board_size and 0 <= position[1] < self.board_size

    def get_empty_space(self, state):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if state.board[row][col] == '0':
                    return row, col
        return -1, -1

    def swap(self, empty_space, piece_moved, state):
        empty_space_i, empty_space_j = empty_space[0], empty_space[1]
        piece_i, piece_j = piece_moved[0], piece_moved[1]
        state.board[piece_i][piece_j], state.board[empty_space_i][empty_space_j] = \
            state.board[empty_space_i][empty_space_j], state.board[piece_i][piece_j]


class State:
    def __init__(self, board, move):
        self.board = board
        self.move = move
