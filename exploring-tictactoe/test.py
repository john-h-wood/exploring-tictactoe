from random import choice
from ttc_theory import flatten_board
from ttc_state import TTCState
from ttc_constants import GAME_TURN_X, GAME_WIN_NONE
from ttc_format import print_board


def print_random_game(state_map):
    working_state = state_map[0]

    while working_state.win_state == GAME_WIN_NONE:
        print_board(working_state.board)
        print()
        random_child_id = choice(working_state.get_children_ids())
        working_state = state_map[random_child_id]

    print_board(working_state.board)


def populate_state_map():
    root_board = flatten_board([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    root_state = TTCState(root_board, GAME_TURN_X)
    state_map = {root_state.id: root_state}

    root_state.recursively_populate_children(state_map)

    return state_map


def main():
    state_map = populate_state_map()
    print_random_game(state_map)


if __name__ == '__main__':
    main()