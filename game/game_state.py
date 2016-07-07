"""
Somehow check to see if king is under check, checkmate, it is stalemate, or draw occurs

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""


def no_moves(position):
    """

    :type position Board
    :return:
    """
    return position.all_possible_moves() is None


def isCheckmate(position, color):
    """

    :param position:
    :param color:
    :return:
    """
    return no_moves(position) and \
        position.piece_at_square(position.find_king(color)).in_check()
