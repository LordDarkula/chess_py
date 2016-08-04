from chess_py.pieces.piece_const import Piece_values
from chess_py.core.color import Color
from copy import deepcopy as cp


class Ai:
    def __init__(self, input_color):
        """
        Creates interface for human player.
        :type input_color: Color
        """
        self.color = input_color
        self.piece_scheme = Piece_values()

    def generate_move(self, position):
        """
        Returns valid and legal move given position
        :type position: Board
        :rtype Move
        """
        print("Running depth search")
        return self.best_move(position, self.color)

    def best_move(self, position, color):
        """
        Finds the best move based on material after the move
        :type position Board
        :type color Color
        :rtype Move
        """
        moves = position.all_possible_moves(input_color=color)
        my_move = moves[0]
        advantage = position.advantage_as_result(my_move, self.piece_scheme)

        for move in moves:
            if position.advantage_as_result(move, self.piece_scheme) > advantage:
                my_move = move
                advantage = position.advantage_as_result(move, self.piece_scheme)

        return my_move

    def depth_search(self, position, depth, color):
        """
        Returns valid and legal move given position
        :type position: Board
        :type depth int
        :type color Color
        :rtype Move
        """
        if depth <= 0:
            moves = position.all_possible_moves(input_color=color)
            my_move = moves[0]
            advantage = position.advantage_as_result(my_move, self.piece_scheme)

            for move in moves:
                if position.advantage_as_result(move, self.piece_scheme) > advantage:
                    my_move = move
                    advantage = position.advantage_as_result(move, self.piece_scheme)

            return my_move

        moves = position.all_possible_moves(input_color=self.color)

        for move in moves:
            test_board = cp(position)
            test_board.update(move)
            return self.depth_search(test_board, depth - 1, Color(not color.color))
