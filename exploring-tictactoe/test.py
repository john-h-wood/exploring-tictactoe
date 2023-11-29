from random import choice
from ttc_theory import flatten_board, compute_win_state
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
    root_state = TTCState(root_board, GAME_TURN_X, True)
    state_map = {root_state.id: root_state}

    root_state.recursively_populate_children(state_map)

    return state_map


def count_end_states(state_map):
    count = 0
    for state in state_map.values():
        if state.win_state != GAME_WIN_NONE:
            count += 1
    return count


def validate_end_states(state_map):
    # Make list of end states
    end_states = list()
    seen_boards = list()

    for state in state_map.values():
        if state.win_state != GAME_WIN_NONE:
            end_states.append(state)
    for end_state in end_states:
        if end_state.board in seen_boards:
            print(f'{end_state} board fails uniqueness')
        seen_boards.append(end_state.board)
        if compute_win_state(end_state.board) == GAME_WIN_NONE:
            print(f'{end_state} board')


def print_relation_stats(state_map):
    maximum_parents = -1

    for state in state_map.values():
        parent_count = len(state.get_parent_ids())

        if parent_count > maximum_parents:
            maximum_parents = parent_count

    print(f'max number of parents: {maximum_parents}')


def main():
    state_map = populate_state_map()
    print_relation_stats(state_map)


if __name__ == '__main__':
    main()