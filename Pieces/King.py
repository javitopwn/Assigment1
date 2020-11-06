import Utils
from Position import Position
from Piece import Piece
from Action import Action


# this class implements the getPossibleActions for each type of piece
# Pawn, Rook, Bishop, Knight, Queen, King
class King(Piece):

    # constructor
    def __init__(self, color):
        self.m_color = color

        if color == 0:
            self.m_type = Utils.wKing
        else:
            self.m_type = Utils.bKing


    # this method must be completed with all the possible pieces
    def getPossibleActions(self , state):       #Given a state I must find all the possibleActions for that state.

        r = state.m_agentPos.row
        c = state.m_agentPos.col
        action = None

        l = []

        oponent_color = -1
        if self.m_color == 0:              # white king
            oponent_color = 1
        elif self.m_color == 1:            # black king
            oponent_color = 0

        if state.m_board[r + 1][c] == Utils.empty or Utils.getColorPiece(state.m_board[r + 1][c]) == oponent_color:        # go down one row
            l.append(Action(state.m_agentPos, Position(r + 1, c)))
        if state.m_board[r - 1][c] == Utils.empty or Utils.getColorPiece(state.m_board[r - 1][c]) == oponent_color:       # go up one row
            l.append(Action(state.m_agentPos, Position(r-1, c)))
        if state.m_board[r + 1][c-1] == Utils.empty or Utils.getColorPiece(state.m_board[r + 1][c-1]) == oponent_color:   # Diagonal move ⭹
            l.append(Action(state.m_agentPos, Position(r + 1, c)))
        if state.m_board[r + 1][c+1] == Utils.empty or Utils.getColorPiece(state.m_board[r + 1][c+1]) == oponent_color:    # Diagonal move  ⭸
            l.append(Action(state.m_agentPos, Position(r-1, c)))
        if state.m_board[r - 1][c-1] == Utils.empty or Utils.getColorPiece(state.m_board[r - 1][c-1]) == oponent_color:   # Diagonal move  ⭶
            l.append(Action(state.m_agentPos, Position(r-1, c)))
        if state.m_board[r - 1][c +1] == Utils.empty or Utils.getColorPiece(state.m_board[r - 1][c +1]) == oponent_color:    # Diagonal move  ⭷
            l.append(Action(state.m_agentPos, Position(r-1, c)))

        return l
