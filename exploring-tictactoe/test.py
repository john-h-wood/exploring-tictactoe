import time
from random import choice
from ttc_theory import flatten_board, compute_win_state, combine_child_win_state
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


def populate_stored_states():
    root_board = flatten_board([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    root_state = TTCState(root_board, GAME_TURN_X)
    stored_states = {root_state.id: root_state}

    root_state.recursively_populate_children(stored_states)

    return stored_states


def count_end_states(stored_states):
    count = 0
    for state in stored_states.values():
        if state.win_state != GAME_WIN_NONE:
            count += 1
    return count


def validate_end_states(stored_states):
    # Make list of end states
    end_states = list()
    seen_boards = list()

    for state in stored_states.values():
        if state.win_state != GAME_WIN_NONE:
            end_states.append(state)
    for end_state in end_states:
        if end_state.board in seen_boards:
            print(f'{end_state} board fails uniqueness')
        seen_boards.append(end_state.board)
        if compute_win_state(end_state.board) == GAME_WIN_NONE:
            print(f'{end_state} board')


def print_relation_stats(stored_states):
    maximum_parents = -1

    for state in stored_states.values():
        parent_count = len(state.parents)

        if parent_count > maximum_parents:
            maximum_parents = parent_count

    print(f'max number of parents: {maximum_parents}')


def main():
    start = time.perf_counter()
    stored_states = populate_stored_states()
    print(f'Time to populate stored states: {round(time.perf_counter() - start, 3)}s')

    TTCState.recursively_calculate_future_win_states(stored_states)

    print(combine_child_win_state(1, 1, 2))

    for state in stored_states.values():
        print(state.future_win_state)


if __name__ == '__main__':
    main()