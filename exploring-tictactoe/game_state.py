class GameState:
    """
    0   1   2
    3   4   5
    6   7   8
    """
    def __init__(self, board, turn):
        self.board = board
        self.turn = turn
        self.win_state = self.compute_win_state()

    def print_board(self):
        for row_index in range(0, 9, 3):
            print(self.board[row_index], self.board[row_index + 1], self.board[row_index + 2])

    def compute_win_state(self):
        # Check horizontals. i is index of row
        for i in range(0, 9, 3):
            if self.board[i] != 0 and (self.board[i] == self.board[i + 1] == self.board[i + 2]):
                return self.board[i]

        # Check verticals. i is index of column
        for i in range(3):
            if self.board[i] != 0 and (self.board[i] == self.board[i + 3] == self.board[i + 6]):
                return self.board[i]

        # Check 0 to 8 diagonal
        if self.board[0] != 0 and (self.board[0] == self.board[4] == self.board[8]):
            return self.board[0]

        # Check 2 to 6 diagonal
        if self.board[2] != 0 and (self.board[2] == self.board[4] == self.board[6]):
            return self.board[2]

        # No wins found. Is board full? Is so, then tie (3). Otherwise, nothing (0)
        return 0 if (0 in self.board) else 3

