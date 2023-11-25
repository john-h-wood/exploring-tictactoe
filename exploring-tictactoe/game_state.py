import copy


class GameState:
    """
    0   1   2
    3   4   5
    6   7   8
    """

    def __init__(self, board, turn, parent_state):
        self.board = board
        self.turn = turn
        self.win_state = self.compute_win_state()
        self.parent_state = parent_state
        self.child_states = None

    def __repr__(self):
        return f'GameState(board={self.board}, ...)'

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

    def find_blank_indices(self):
        blank_indices = list()
        for space_index, space_state in enumerate(self.board):
            if space_state == 0:
                blank_indices.append(space_index)
        return blank_indices

    def populate_child_states(self):
        # Create children list if it doesn't exist
        if self.child_states is None:
            self.child_states = list()
            # There are only children if this isn't an end state
            if self.win_state == 0:
                next_turn = 1 if (self.turn == 2) else 2

                for blank_index in self.find_blank_indices():
                    child_board = copy.copy(self.board)
                    child_board[blank_index] = self.turn
                    child_state = GameState(child_board, next_turn, self)

                    self.child_states.append(child_state)
        else:
            raise ValueError(f'{self} already has populated children')

    def recursively_populate_child_states(self):
        if self.child_states is None:
            self.populate_child_states()

        for child_state in self.child_states:
            child_state.recursively_populate_child_states()

    def recursively_find_child_end_states(self):
        child_end_states = list()

        for child_state in self.child_states:
            if child_state.win_state != 0:
                child_end_states.append(child_state)
            else:
                child_end_states.extend(child_state.recursively_find_child_end_states())

        return child_end_states


