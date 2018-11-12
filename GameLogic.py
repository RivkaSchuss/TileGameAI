from copy import copy, deepcopy
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
        empty_space = self.get_empty_space(state)
        piece_above = empty_space[0] - 1, empty_space[1]
        piece_below = empty_space[0] + 1, empty_space[1]
        piece_right = empty_space[0], empty_space[1] + 1
        piece_left = empty_space[0], empty_space[1] - 1
        # move up
        if self.check_valid(piece_below):
            copied = deepcopy(state.board)
            self.swap(empty_space, piece_below, copied)
            state_to_add = State(copied, 'U')
            result.append(state_to_add)
        # move down
        if self.check_valid(piece_above):
            copied = deepcopy(state.board)
            self.swap(empty_space, piece_above, copied)
            state_to_add = State(copied, 'D')
            result.append(state_to_add)
        # move left
        if self.check_valid(piece_right):
            copied = deepcopy(state.board)
            self.swap(empty_space, piece_right, copied)
            state_to_add = State(copied, 'L')
            result.append(state_to_add)
        # move right
        if self.check_valid(piece_left):
            copied = deepcopy(state.board)
            self.swap(empty_space, piece_left, copied)
            state_to_add = State(copied, 'R')
            result.append(state_to_add)
        return result

    def construct_path(self, father, path_formed):
        action_list = list()

        while path_formed[father].move is not None:
            father = path_formed[father]
            action_list.append(father.move)

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

    def swap(self, empty_space, piece_moved, board):
        empty_space_i, empty_space_j = empty_space[0], empty_space[1]
        piece_i, piece_j = piece_moved[0], piece_moved[1]
        board[piece_i][piece_j], board[empty_space_i][empty_space_j] = \
            board[empty_space_i][empty_space_j], board[piece_i][piece_j]


class State:
    def __init__(self, board, move):
        self.board = board
        self.move = move
