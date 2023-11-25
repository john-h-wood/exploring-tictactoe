import random

from game_state import GameState, end_states


def convert_board(board):
    new_board = list()
    for row in board:
        new_board.extend(row)
    return new_board



start_board = convert_board([[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]])
start_state = GameState(start_board, 1, None)

start_state.recursively_populate_child_states()


# def show_random_game():
#     working_state = start_state
#     while working_state.win_state == 0:
#         working_state.print_board()
#
#         random_child_index = random.randint(0, len(working_state.child_states) - 1)
#         working_state = working_state.child_states[random_child_index]
#         print()
#     working_state.print_board()
#     print(f'{working_state.win_state} wins')
#     print()


# while True:
#     show_random_game()
#     _ = input('input anything to see another game')


for end_state in end_states:
    end_state.print_board()
    print()
