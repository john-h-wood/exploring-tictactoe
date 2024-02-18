from state import TTCState
from constants import CELL_EMPTY, TURN_X, WIN_NONE
from format import print_board
from random import choice


def print_random_game(start_state: TTCState):
    working_state = start_state
    while working_state.win_state == WIN_NONE:
        print_board(working_state.board)
        print()
        working_state = choice(working_state.children)

    print_board(working_state.board)
    print(f'Final win state: {working_state.win_state}')


def main():
    stored_states = [{} for _ in range(10)]
    empty_board = [CELL_EMPTY for _ in range(9)]
    root_state = TTCState(empty_board, TURN_X, 0)

    root_state.recursively_populate_children(stored_states)

    print_random_game(root_state)


if __name__ == '__main__':
    main()