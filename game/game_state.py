"""
Somehow check to see if king is under check, checkmate, it is stalemate, or draw occurs

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""


def isStalemate(position):
    """

    :type position Board
    :return:
    """
    return position.all_possible_moves() is None


def isCheckmate(position):
    pass
