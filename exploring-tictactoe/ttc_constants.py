# ============ CONSTANTS ===============================================================================================
# CELL STATES
CELL_X = 1
CELL_O = 2
CELL_EMPTY = 0
CELL_STATE_COUNT = 3

# WIN STATES
WIN_X = CELL_X
WIN_O = CELL_O
WIN_TIE = 3
WIN_NONE = 0

# TURN
TURN_X = 1
TURN_O = 2

# POSSIBILITIES
POSS_DESCRIPTIONS = {
    'POSS_G_TIE': 'All child states have POSS_G_TIE and if they don\'t have children, '
                  'they have WIN_TIE',
    'POSS_G_X_WIN': 'All child states have POSS_G_X_WIN and if they don\'t have children, '
                    'they have WIN_X',
    'POSS_G_O_WIN': 'All child states have POSS_G_O_WIN and if they don\'t have children, '
                    'they have WIN_O',
    'POSS_C_X_WIN': 'Given specific child selections on states with TURN_X,'
                    'there exists a path from this state to one with WIN_X',
    'POSS_C_O_WIN': 'Given specific child selections on states with TURN_O,'
                    'there exists a path from this state to one with WIN_O',
    'POSS_C_X_TIE': 'Given specific child selections on states with TURN_X,'
                    'there exists a path from this state to one with WIN_TIE',
    'POSS_C_O_TIE': 'Given specific child selections on states with TURN_O,'
                    'there exists a path from this state to one with WIN_TIE'
}

POSS_G_TIE = 0
POSS_G_X_WIN = 1
POSS_G_O_WIN = 2

POSS_C_X_WIN = 3
POSS_C_O_WIN = 4
POSS_C_X_TIE = 5
POSS_C_O_TIE = 6
