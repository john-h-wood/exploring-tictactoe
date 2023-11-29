from ttc_theory import flatten_board
from ttc_state import TTCState
from ttc_constants import GAME_TURN_X

board = flatten_board([[2, 1, 2], [0, 0, 1], [1, 2, 1]])

board_state = TTCState(board, GAME_TURN_X)
print(board_state.id, board_state.win_state)
