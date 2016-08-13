from chess_py.pieces.piece_const import Piece_values
from chess_py.core.color import Color
from copy import deepcopy as cp
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
        return self.treeSearch(position, 1, self.color)[0]

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

        return my_move

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
        return reply, test.advantage_as_result(reply, self.piece_scheme)

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

    def treeSearch(self, position, depth, color):
        """
        Returns valid and legal move given position
        :type position: Board
        :type depth int
        :type color Color
        :rtype Move
        """
        moves = position.all_possible_moves(color)
        if depth == 0:
            worst = self.best_reply(position.all_possible_moves(color)[0], position)
            worst_index = 0
            for i in range(len(moves)):
                print("In the tree search for")
                if worst[1] > self.best_reply(moves[i], position)[1]:
                    worst = self.best_reply(moves[i], position)
                    worst_index = i
            print("depth: 0")
            return moves[worst_index], worst[1]

        else:
            worst = self.treeSearch(self.one_move_ahead(position.all_possible_moves(color)[0], position),
                                    depth - 1,
                                    color)

            worst_index = 0
            for i in range(len(moves)):
                if self.best_reply(moves[i], position)[1] > 6:
                    pot_worst = self.treeSearch(self.one_move_ahead(position.all_possible_moves(color)[0], position),
                                                depth - 1,
                                                color)
                if worst[1] > pot_worst[1]:
                    worst = pot_worst
                    worst_index = i
            print("depth: ", depth)

            return moves[worst_index], worst[1]

    def one_move_ahead(self, move, position):
        test = cp(position)
        test.update(move)
        test.update(self.best_move(test, move.color.opponent()))
        return test


