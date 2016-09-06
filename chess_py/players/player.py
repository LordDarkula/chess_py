# -*- coding: utf-8 -*-

"""
Parent class for all Players.
"""

from abc import ABCMeta, abstractmethod


class PLayer:
    __metaclass__ = ABCMeta

    def __init__(self, input_color):
        """
        Creates interface for base player.
        :type input_color: Color
        """
        self.color = input_color

    @abstractmethod
    def generate_move(self, position):
        """
        Returns valid and legal move given position
        :type position: Board
        :rtype Move
        """
        pass

