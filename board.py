from constants import *

class Board:

    def __init__(self, fen=startFEN):
        self.board, self.currColor, self.castleRights, self.enPassantSquare, self.fiftyPlyCounter, self.moveCounter = self.parseFen(fen)

    def parseFen(self, fen):
        board, currColor, castleRights, enPassantSquare, fiftyPlyCounter, moveCounter = fen.split(' ')

        board = self.translateToInternalState(board)
        currColor = WHITE if currColor == 'w' else BLACK
        castleRights = self.parseCastleRights(castleRights)
        enPassantSquare = self.indexOfSquare(enPassantSquare)
        fiftyPlyCounter = int(fiftyPlyCounter)
        moveCounter = int(moveCounter)


        return board, currColor, castleRights, enPassantSquare, fiftyPlyCounter, moveCounter

    # Get the index 0-63 of the square given in chess notation
    # If given - return None
    # e.g e2 -> 42
    def indexOfSquare(self, sqr):
        return None if sqr == '-' else ord(sqr[0]) - 97 + (RANKS - int(sqr[1])) * 8

    # Translate a FEN position to an array of pieces
    def translateToInternalState(self, pos):
        board = []
        for p in pos:
            if p.isdigit():
                for i in range(int(p)):
                    board.append(0)
            else:
                c = p.lower()
                color = WHITE if p.isupper() else BLACK

                if c == 'p':
                    board.append(PAWN | color)

                elif c == 'n':
                    board.append(KNIGHT | color)

                elif c == 'b':
                    board.append(BISHOP | color)
        
                elif c == 'r':
                    board.append(ROOK | color)
        
                elif c == 'q':
                    board.append(QUEEN | color)
        
                elif c == 'k':
                    board.append(KING |color)

        return board

    # Get the notational letter of a piece
    def letter(self, piece):
        if piece == 0:
            return '0'

        else:
            b = format(piece, "05b")
            color, p_type = int(b[:2], 2) * 8, int(b[2:], 2)

            if p_type == PAWN:
                return 'P' if color == WHITE else 'p'

            if p_type == KNIGHT:
                return 'N' if color == WHITE else 'n'
            
            if p_type == BISHOP:
                return 'B' if color == WHITE else 'b'

            if p_type == ROOK:
                return 'R' if color == WHITE else 'r'

            if p_type == QUEEN:
                return 'Q' if color == WHITE else 'q'

            if p_type == KING:
                return 'K' if color == WHITE else 'k'

    # Returns a tuple of True and False according to the FEN
    # e.g KQq -> True, True, False, True
    # Explanation: K exist, Q exists, k doesn't exist, q exists
    def parseCastleRights(self, s):
        return 'K' in s, 'Q' in s, 'k' in s, 'q' in s
        
    def printState(self):
        for i, piece in enumerate(self.board):
            print(self.letter(piece), end=('\n' if (i + 1) % RANKS == 0 else ' '))

    def validateMove(self, move):
        return True

    def makeMove(self, move, inSearch=False):
        if not self.validateMove(move):
            return -1

        startSquare = self.indexOfSquare(move.startSquare)
        targetSquare = self.indexOfSquare(move.targetSquare)

        self.board[startSquare], self.board[targetSquare] = 0, self.board[startSquare]
        return 1

