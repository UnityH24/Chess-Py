class Move:

    F_CAPTURE = 0
    F_CASTLES_K = 1
    F_CASTLES_Q = 2
    F_ENPASSANT = 3
    F_PROMOTION = 4

    def __init__(self, startSquare, targetSquare, flags=None):
        self.startSquare = startSquare
        self.targetSquare = targetSquare
        self.flags = flags
