# program to generate sudoku

import tabulate
import random

class Board:

    def __init__(self):
        # create the board
        self.board = [['*' for x in range(9)] for y in range(9)]

    def getBoard(self):
        # return nested list board object
        return self.board

    def printBoard(self):
        # pretty-print the board using tabulate
        print(tabulate(self.getBoard()))

    def transpose(self):
        # return a transpose of the board
        return [[self.board[j][i] for j in range(9)] for i in range(9)]


    def is_segment_valid(segment):
        # check if a segment contains repeated values in range 1-9
        segmap = {x:0 for x in range(9)}

if __name__ == '__main__':
    b = Board()
    b.printBoard()


