from constants import *


# ============ FUNCTIONS ON BOARD ======================================================================================
def flatten_board(board):
    new_board = list()
    for row in board:
        new_board.extend(row)
    return new_board


def board_to_int(board):
    total = 0
    for exponent, value in enumerate(board[::-1]):
        total += value * (CELL_STATE_COUNT ** exponent)
    return total


# ============ FUNCTIONS ON GAME =======================================================================================
def compute_win_state(board):
    # RELIES ON
    # GAME_WIN_X = CELL_X
    # GAME_WIN_O = CELL_O
    # in ttc_constants?

    # Check horizontals. i is index of row
    for i in range(0, 9, 3):
        if board[i] != 0 and (board[i] == board[i + 1] == board[i + 2]):
            return board[i]

    # Check verticals. i is index of column
    for i in range(3):
        if board[i] != 0 and (board[i] == board[i + 3] == board[i + 6]):
            return board[i]

    # Check 0 to 8 diagonal
    if board[0] != 0 and (board[0] == board[4] == board[8]):
        return board[0]

    # Check 2 to 6 diagonal
    if board[2] != 0 and (board[2] == board[4] == board[6]):
        return board[2]

    # No wins found. Is board full? Is so, then tie (3). Otherwise, nothing (0)
    return 0 if (0 in board) else 3


def combine_child_win_state(turn, win_state, child_win_state):
    # a==b -> a
    # both are tie -> tie (captured by above)
    # one tie -> at least tie for whoever's turn it for the parent
    # otherwise, can't tell
    win_states = (win_state, child_win_state)
    if win_state == child_win_state:
        return win_state

    elif WIN_TIE in win_states:
        if turn == TURN_X:
            return GAME_WIN_TIE_POSSIBILITY_X
        return GAME_WIN_TIE_POSSIBILITY_O

    elif (WIN_X in win_states) and turn == TURN_X:
        return WIN_X

    elif (WIN_O in win_states) and turn == TURN_O:
        return WIN_O

    return WIN_NONE
