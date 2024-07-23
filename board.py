#!/usr/bin/env python3

from enum import Enum
from itertools import count

DIM = "\033[2m"
RESET = "\033[0m"
BLACK_ON_WHITE = "\033[1;30;47m"
WHITE_ON_BLACK = "\033[1;37;40m"


class Colour(Enum):
    """
    Represents piece or board square colour.
    """
    WHITE = 0, BLACK_ON_WHITE
    BLACK = 1, WHITE_ON_BLACK

    def __new__(cls, value, sq_ansi):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.sq_ansi = sq_ansi
        return obj

    def other(self):
        return Colour.BLACK if self == Colour.WHITE else Colour.WHITE


class Piece:
    """
    Represents a chess piece including pawn, of no specific colour
    """
    def __init__(self, name, letter, solid, outline):
        super().__init__()
        self.name = name
        self.letter = letter
        self.outline = outline
        self.solid = solid

    def ascii(self, colour):
        return self.letter if colour == Colour.BLACK else self.letter.upper()


# white piece letters are UPPER CASE ASCII, black are lower case
# unicode escapes are chess pieces in solid and outline (although officially named black and white)
PAWN = Piece("pawn", 'p', "\u265F", "\u2659")
ROOK = Piece("rook", 'r', "\u265C", "\u2656")
KNIGHT = Piece("knight", 'n', "\u265E", "\u2658")
BISHOP = Piece("bishop", 'b', "\u265D", "\u2657")
QUEEN = Piece("queen", 'q', "\u265B", "\u2655")
KING = Piece("king", 'k', "\u265A", "\u2654")


def init_board():

    def b(piece):
        return Colour.BLACK, piece

    def w(piece):
        return Colour.WHITE, piece

    return [
        [b(ROOK), b(KNIGHT), b(BISHOP), b(QUEEN), b(KING), b(BISHOP), b(KNIGHT), b(ROOK)],
        [b(PAWN), b(PAWN),   b(PAWN),   b(PAWN),  b(PAWN), b(PAWN),   b(PAWN),   b(PAWN)],
        [None,    None,      None,      None,     None,    None,      None,      None],
        [None,    None,      None,      None,     None,    None,      None,      None],
        [None,    None,      None,      None,     None,    None,      None,      None],
        [None,    None,      None,      None,     None,    None,      None,      None],
        [w(PAWN), w(PAWN),   w(PAWN),   w(PAWN),  w(PAWN), w(PAWN),   w(PAWN),   w(PAWN)],
        [w(ROOK), w(KNIGHT), w(BISHOP), w(QUEEN), w(KING), w(BISHOP), w(KNIGHT), w(ROOK)],
    ]


def square_unicode(colour_piece, square_colour):
    """
    returns unicode piece ansi string for chess square occupied by colour_piece (None or tuple of Colour, Piece)
    """
    ch = " "
    if colour_piece is not None:
        ch = colour_piece[1].outline if colour_piece[0] == square_colour else colour_piece[1].solid
    return f"{square_colour.sq_ansi}{ch}"


def square_ascii(colour_piece, square_colour):
    """
    returns ascii piece ansi string for chess square occupied by colour_piece (None or tuple of Colour, Piece)
    """
    ch = " " if colour_piece is None else colour_piece[1].ascii(colour_piece[0])
    return f"{square_colour.sq_ansi}{ch}"


def print_board(board, render_square):
    """print board using render_square with black pieces at top"""
    sq_colour = Colour.WHITE
    for i, rank in zip(count(), board):
        for j, file in zip(count(), board[i]):
            print(render_square(board[i][j], sq_colour), end="")
            sq_colour = sq_colour.other()
        sq_colour = sq_colour.other()
        print(f"{RESET} {DIM}{8 - i}{RESET}")
    print(f"{DIM}ABCDEFGH{RESET}")


# just print initial board in both ascii and unicode
if __name__ == '__main__':
    brd = init_board()
    print()
    print_board(brd, square_ascii)
    print()
    print_board(brd, square_unicode)
