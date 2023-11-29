from ttc_theory import flatten_board
from ttc_state import TTCState
from ttc_constants import GAME_TURN_X, GAME_WIN_NONE

root_board = flatten_board([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
root_state = TTCState(root_board, GAME_TURN_X)

state_map = {root_state.id: root_state}

root_state.recursively_populate_children(state_map)
print(len(state_map))

def print_random_game(state_map, root_state):
    working_state = root_state
    while working_state.win_state != GAME_WIN_NONE:

