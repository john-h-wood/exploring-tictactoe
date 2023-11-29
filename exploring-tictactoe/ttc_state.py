import ttc_theory as theory


class TTCState:
    def __init__(self, board, turn):
        # State identity
        self.id = theory.board_to_int(board)
        self.board = board
        self.turn = turn
        self.win_state = theory.compute_win_state(board)

        # State relations (lazily computed)
        self.parents = None
        self.children = None

