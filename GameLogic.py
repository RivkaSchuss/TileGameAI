from copy import deepcopy


class GameLogic(object):

    def __init__(self, state, board_size):
        self.state = state
        self.board_size = board_size

    def get_initial_state(self):
        return self.state

    """
    checks if we've arrived at the goal state
    """
    def goal_state_check(self, state):
        count = 1
        for row in state.board:
            for node in row:
                if node != '0' and node != str(count):
                    return False
                count += 1
        return True

    """
    gets the next possible moves for the current node
    """
    def get_next_moves(self, state):
        result = list()
        empty_space = self.get_empty_space(state)
        # defining the pieces surrounding the empty space
        piece_above = empty_space[0] - 1, empty_space[1]
        piece_below = empty_space[0] + 1, empty_space[1]
        piece_right = empty_space[0], empty_space[1] + 1
        piece_left = empty_space[0], empty_space[1] - 1
        # move up
        if self.check_valid(piece_below):
            copied = deepcopy(state.board)
            self.swap(empty_space, piece_below, copied)
            state_to_add = State(copied, 'U', state)
            result.append(state_to_add)
        # move down
        if self.check_valid(piece_above):
            copied = deepcopy(state.board)
            self.swap(empty_space, piece_above, copied)
            state_to_add = State(copied, 'D', state)
            result.append(state_to_add)
        # move left
        if self.check_valid(piece_right):
            copied = deepcopy(state.board)
            self.swap(empty_space, piece_right, copied)
            state_to_add = State(copied, 'L', state)
            result.append(state_to_add)
        # move right
        if self.check_valid(piece_left):
            copied = deepcopy(state.board)
            self.swap(empty_space, piece_left, copied)
            state_to_add = State(copied, 'R', state)
            result.append(state_to_add)
        return result

    """
    backtracks and constructs the path based on the actions performed to arrive
    at the goal state
    """
    def construct_path(self, final_state):
        action_list = []
        current_node = final_state

        while current_node.previous is not None:
            action_list.insert(0, current_node.move)
            current_node = current_node.previous

        return action_list

    # checks if the move is a valid move
    def check_valid(self, position):
        return 0 <= position[0] < self.board_size and 0 <= position[1] < self.board_size

    """
    find the empty space on the board
    """
    def get_empty_space(self, state):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if state.board[row][col] == '0':
                    return row, col
        return -1, -1

    """
    swaps the piece to move with the empty space
    """
    def swap(self, empty_space, piece_moved, board):
        empty_space_i, empty_space_j = empty_space[0], empty_space[1]
        piece_i, piece_j = piece_moved[0], piece_moved[1]
        board[piece_i][piece_j], board[empty_space_i][empty_space_j] = \
            board[empty_space_i][empty_space_j], board[piece_i][piece_j]


"""
defining a class state to hold the game board as well as other properties
"""


class State:
    def __init__(self, board, move=None, previous=None, depth=0, heuristic=0):
        self.board = board
        self.move = move
        self.previous = previous
        self.depth = depth
        self.heuristic = heuristic

    @property
    def get_f(self):
        return self.depth + self.heuristic

    def __hash__(self):
        return hash(str(self.board))


