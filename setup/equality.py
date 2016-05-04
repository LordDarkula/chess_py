"""
Class that contains all equality comparison methods specific for chess_py
"""

from setup.algebraic_notation import algebraic


def location_not_none(location):

    """
    Determines whether location exists.
    :type location: algebraic.Location
    :rtype bool
    """
    return location is not None and location.rank is not None and location.file is not None

def move_not_none(move):

    """
    Determines whether move exists.
    :type move: algebraic.move
    :rtype bool
    """
    return move is not None and move.rank is not None and move.file is not None and move.piece is not None

def piece_matches_description(piece, reference_type, reference_color):

    """
    Determines whether piece matches reference description.
    :type piece: pieces *
    :type reference_type: pieces *
    :type reference_color: str
    :rtype bool
    """
    return type(piece) is reference_type and piece.white == reference_color is "white"

def piece_equals(piece1, piece2):

    """
    Determines whether piece1 and piece2 are "equal", that is are they are the same type and color.
    :type piece1: pieces *
    :type piece2: pieces *
    :rtype bool
    """
    return type(piece1) == type(piece2) and piece1.white == piece2.white

def find_piece(piece, position):

    """
    Locates all instances of pieces in position that match piece.
    :type piece: pieces *
    :type position: board.Board
    :rtype list containing algebraic.Location
    """
    pieces = []

    for i in range(7):

        for j in range(7):

            if piece.equals(position.position[i][j]):
                pieces.append(algebraic.Location(i, j))

    return pieces
