#!/usr/bin/env python3

from enum import Enum
from itertools import count

# unicode outline
outline_king = "\u2654"
outline_queen = "\u2655"
outline_rook = "\u2656"
outline_bishop = "\u2657"
outline_knight = "\u2658"
outline_pawn = "\u2659"
# unicode solid
solid_king = "\u265A"
solid_queen = "\u265B"
solid_rook = "\u265C"
solid_bishop = "\u265D"
solid_knight = "\u265E"
solid_pawn = "\u265F"

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


# white pieces are UPPER CASE ASCII, black are lower case
PAWN = Piece("pawn", 'p', solid_pawn, outline_pawn)
ROOK = Piece("rook", 'r', solid_rook, outline_rook)
KNIGHT = Piece("knight", 'n', solid_knight, outline_knight)
BISHOP = Piece("bishop", 'b', solid_bishop, outline_bishop)
QUEEN = Piece("queen", 'q', solid_queen, outline_queen)
KING = Piece("king", 'k', solid_king, outline_king)


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
