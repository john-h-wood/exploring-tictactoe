
"""
X | X | X  
---------
X | X | X
---------
X | X | X
"""

"""
0   1   2
3   4   5
6   7   8
"""


def print_board(board):
    for row in range(0, 9, 3):
        print(board[row], board[row + 1], board[row + 2])