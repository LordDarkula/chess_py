# -*- coding: utf-8 -*-

from chess_py.pieces.piece_const import Piece_values
from chess_py.core.color import Color
from copy import deepcopy as cp
from chess_py.core.algebraic import notation_const
from chess_py.players.tree import Tree


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
        position.out()
        print("Running tree search")
        if self.is_quiet_position(input_color=self.color, position=position):
            return position.all_possible_moves(self.color)[int(len(position.all_possible_moves(self.color))/2)]
        else:
            move = self.treeSearch(position, 3, self.color)
            print("Final advantage ", move[1])
            return move[0]

    @staticmethod
    def is_quiet_position(input_color, position):
        for move in position.all_possible_moves(input_color):
            if move.status == notation_const.CAPTURE or \
                    move.status == notation_const.CAPTURE_AND_PROMOTE:
                return False

        for move in position.all_possible_moves(input_color.opponent()):
            if move.status == notation_const.CAPTURE or \
                            move.status == notation_const.CAPTURE_AND_PROMOTE:
                return False

        return True

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
            # print("In the best move for")
            if position.advantage_as_result(move, self.piece_scheme) > advantage:

                my_move = move
                advantage = position.advantage_as_result(move, self.piece_scheme)

        return my_move, advantage

    def best_reply(self, move, position):
        """
        Finds the best move based on material after the move
        :type move Move
        :type position Board
        :rtype Move
        """
        test = cp(position)
        test.update(move)
        reply = self.best_move(test, move.color.opponent())
        return reply, test.advantage_as_result(reply[0], self.piece_scheme)



#TODO if pot_worst is the same as worst decide which move is better for me
#TODO safegard against checkmate
#TODO build move tree to avoid long wait

    def treeSearch(self, position, depth, color):
        """
        Returns valid and legal move given position
        :type position: Board
        :type depth int
        :type color Color
        :rtype Move
        """
        print("Depth: ", depth)
        if depth == 1:
            return self.best_move(position, color)

        moves = position.all_possible_moves(color)
        print("Number of possible moves", len(moves))

        my_move = None
        for move in moves:
            move.out()
            test = cp(position)
            test.update(move)
            if len(test.all_possible_moves(color.opponent())) == 0:
                return move, 100
            best_reply = self.treeSearch(test, depth=depth-1, color=color.opponent())
            best_reply[0].out()
            print("My Advantage", -best_reply[1])
            if my_move is None or my_move[1] < -best_reply[1]:
                my_move = move, -best_reply[1]

        return my_move

    def weed_checkmate(self, moves, position):
        print("weeding 0ut checkmate")
        final = []
        for i in range(len(moves)):
            test = cp(position)
            test.update(moves[i])

            if not self.best_reply(moves[i], position)[1] == 100:
                final.append(moves[i])

        if len(final) == 0:
            final.append(moves[0])

        return final

    def one_move_ahead(self, move, position):
        test = cp(position)
        test.update(move)
        test.update(self.best_move(test, move.color.opponent()))
        return test


