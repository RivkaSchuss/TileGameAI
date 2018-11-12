from Astar import Astar
from BFS import BFS
from IDS import IDS
from GameLogic import GameLogic
from GameLogic import State


def run_algorithm(algorithm, board, board_size):

    logic = GameLogic(State(board, None, None), board_size)
    if algorithm == 1:
        ids = IDS(State(board, None, None), logic)
        chosen = ids.run_search()
    elif algorithm == 2:
        bfs = BFS(State(board, None, None), logic)
        chosen = bfs.run_search()
    elif algorithm == 3:
        a_star = Astar(State(board, None, None), logic)
        chosen = a_star.run_search()
    else:
        raise Exception("No algorithm was chosen")
    if chosen is not None:
        to_print = ' '.join(map(str, chosen))
        with open('output.txt', 'w') as output_file:
            output_file.write(to_print)


def create_board(board_size, board_string):
    board = []
    board_parsed = board_string.split('-')
    for row in range(board_size):
        added_row = []
        for col in range(board_size):
            added_row.append(board_parsed[row * board_size + col])
        board.append(added_row)
    return board


def main():
    with open('input.txt') as input_file:
        args = input_file.read().splitlines()

    algorithm = int(args[0])
    board_size = int(args[1])
    board = create_board(board_size, args[2])
    print board
    run_algorithm(algorithm, board, board_size)


if __name__ == '__main__':
    main()
