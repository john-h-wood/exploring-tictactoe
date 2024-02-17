from ttc_constants import GAME_WIN_NONE, CELL_EMPTY, GAME_TURN_X, GAME_TURN_O
from ttc_theory import compute_win_state, board_to_int, combine_child_win_state
from copy import copy

# TODO add typing everywhere. It helps, eg gives relevant methods

chain_count = 0


class TTCState:
    # ============ SPECIAL FUNCTIONS ===================================================================================
    def __init__(self, board, turn):
        # State identity
        self.id = board_to_int(board)
        self.board = board
        self.turn = turn
        self.win_state = compute_win_state(board)

        # State relations
        self.parents: list[TTCState] = list()
        self.children: list[TTCState] = list()

        # Future calculation
        self.future_win_state = None

    def __repr__(self):
        return f'TTCState({self.board}, {self.turn})'

    # ============ POPULATION FUNCTIONS ================================================================================

    def find_empty_cell_indices(self):
        empty_cells_indices = list()
        for cell_index, cell_value in enumerate(self.board):
            if cell_value == CELL_EMPTY:
                empty_cells_indices.append(cell_index)
        return empty_cells_indices

    def populate_children(self, stored_states):
        # TODO make stored_state optional
        # TODO make check for if children or parents have already been updated?
        if self.win_state != GAME_WIN_NONE:
            return

        # Create children by processing move
        for empty_cell_index in self.find_empty_cell_indices():
            child_board = copy(self.board)
            child_board[empty_cell_index] = self.turn
            child_id = board_to_int(child_board)

            # Update state map
            # If child exists in map, add parent reference
            if child_id in stored_states:
                stored_states[child_id].parents.append(self)
            # Otherwise, create new game state
            else:
                child_turn = GAME_TURN_X if (self.turn == GAME_TURN_O) else GAME_TURN_O
                child_state = TTCState(child_board, child_turn)
                child_state.parents.append(self)

                stored_states[child_id] = child_state

            # Update this state's children ids
            self.children.append(stored_states[child_id])

    def recursively_populate_children(self, stored_states):
        # Must do self children if they haven't been done
        if len(self.children) == 0 and self.win_state == GAME_WIN_NONE:
            self.populate_children(stored_states)
        for child in self.children:
            child.recursively_populate_children(stored_states)
