#! /data/data/com.termux/files/usr/bin/python
from board import Board
from move import Move


board = Board()

board.printState()

print("———————————")

move = Move("e2", "e4")

board.makeMove(move)

board.printState()
