from ttc_constants import GAME_WIN_NONE, CELL_EMPTY, GAME_TURN_X, GAME_TURN_O
from ttc_theory import compute_win_state, board_to_int
from copy import copy


class TTCState:
    # ============ SPECIAL FUNCTIONS ===================================================================================
    def __init__(self, board, turn):
        # State identity
        self.id = board_to_int(board)
        self.board = board
        self.turn = turn
        self.win_state = compute_win_state(board)

        # State relations (lazily computed)
        self._parent_ids = None
        self._children_ids = None

    def __repr__(self):
        return f'TTCState({self.board}, {self.turn})'

    # ============ RELATIONS FUNCTIONS =================================================================================
    def get_parent_ids(self):
        if self._parent_ids is None:
            raise Exception(f'{self} parent state ids have not been populated')
        return self._parent_ids

    def get_children_ids(self):
        if self._children_ids is None:
            raise Exception(f'{self} child state ids have not been populated')
        return self._children_ids

    def add_parent_id(self, parent_id):
        if self._parent_ids is None:
            self._parent_ids = list()
        self._parent_ids.append(parent_id)

    def add_child_id(self, child_id):
        if self._children_ids is None:
            self._children_ids = list()
        self._children_ids.append(child_id)

    # ============ POPULATION FUNCTIONS ================================================================================

    def find_empty_cell_indices(self):
        empty_cells_indices = list()
        for cell_index, cell_value in enumerate(self.board):
            if cell_value == CELL_EMPTY:
                empty_cells_indices.append(cell_index)
        return empty_cells_indices

    def populate_children(self, state_map):
        if self._children_ids is not None:
            raise Exception(f'{self} child states have already been populated')
        if (self.win_state != GAME_WIN_NONE) and self._children_ids is None:
            self._children_ids = list()

        # Create children by processing move
        for empty_cell_index in self.find_empty_cell_indices():
            child_board = copy(self.board)
            child_board[empty_cell_index] = self.turn
            child_id = board_to_int(child_board)

            # Update state map
            # If child exists in map, add parent reference
            if child_id in state_map:
                state_map[child_id].add_parent_id(self.id)
            # Otherwise, create new game state
            else:
                child_turn = GAME_TURN_X if (self.turn == GAME_TURN_O) else GAME_TURN_O
                child_state = TTCState(child_board, child_turn)
                child_state.add_parent_id(self.id)

                state_map[child_id] = child_state

            # Update this state's children ids
            self.add_child_id(child_id)

    def recursively_populate_children(self, state_map):
        if self._children_ids is None:
            self.populate_children(state_map)
        for child_id in self._children_ids:
            state_map[child_id].recursively_populate_children(state_map)




