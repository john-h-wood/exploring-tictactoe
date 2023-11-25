import copy

from game_state import GameState
import numpy as np


def convert_board(board):
    new_board = list()
    for row in board:
        new_board.extend(row)
    return new_board

def compute_win_state(state):
    # Check horizontals. i is index of row
    for i in range(0, 9, 3):
        if state.board[i] != 0 and (state.board[i] == state.board[i + 1] == state.board[i + 2]):
            return state.board[i]

    # Check verticals. i is index of column
    for i in range(3):
        if state.board[i] != 0 and (state.board[i] == state.board[i + 3] == state.board[i + 6]):
            return state.board[i]

    # Check 0 to 8 diagonal
    if state.board[0] != 0 and (state.board[0] == state.board[4] == state.board[8]):
        return state.board[0]

    # Check 2 to 6 diagonal
    if state.board[2] != 0 and (state.board[2] == state.board[4] == state.board[6]):
        return state.board[2]

    # No wins found. Is board full? Is so, then tie (3). Otherwise, nothing (0)
    return 0 if (0 in state.board) else 3


def validate_end_states(end_states):
    end_boards = [end_state.board for end_state in end_states]
    for index, end_state in enumerate(end_states):
        if compute_win_state(end_state) == 0:
            print(end_state, 'fails win state check')
        if end_boards.count(end_state.board) != 1:
            print(end_state, 'fails uniqueness check:', end_boards.count(end_state.board))


def show_state_history(state):
    i = 0
    working_state = state
    while working_state.parent_state is not None:
        working_state.print_board()
        print(i)
        print()
        working_state = working_state.parent_state
        i += 1
    working_state.print_board()
    print(i)


def rindex(value, ls):
    return len(ls) - 1 - ls[::-1].index(value)


def show_multiple_ways(end_boards, end_states):
    board = [1, 2, 1, 2, 1, 2, 1, 0, 0]
    first_index = end_boards.index(board)
    last_index = rindex(board, end_boards)

    show_state_history(end_states[first_index])
    print('-' * 20)
    show_state_history(end_states[last_index])


def main():
    start_board = convert_board([[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])
    start_state = GameState(start_board, 1, None)
    start_state.recursively_populate_child_states()

    end_states = start_state.recursively_find_child_end_states()
    end_boards = [end_state.board for end_state in end_states]

    end_boards = np.array(end_boards)
    unique_end_boards = np.unique(end_boards, axis=0)
    print(len(unique_end_boards))




if __name__ == '__main__':
    main()