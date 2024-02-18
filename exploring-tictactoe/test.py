from state import TTCState
from constants import CELL_EMPTY, TURN_X
from format import print_board


def main():
    stored_states = [{} for _ in range(10)]
    empty_board = [CELL_EMPTY for _ in range(9)]
    root_state = TTCState(empty_board, TURN_X, 0)

    root_state.recursively_populate_children(stored_states)
    print_board(root_state.board)


if __name__ == '__main__':
    main()