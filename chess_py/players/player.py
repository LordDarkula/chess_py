# -*- coding: utf-8 -*-

"""
Parent class of chess engines built on chess_py. This class must be inherited
and abstract method ``generate_move(self, position) must be implemented.``.
"""

from abc import ABCMeta, abstractmethod
from pip._vendor.distlib.compat import raw_input
import sys


class Player:
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
        Must be implemented by classes that extend ``Player``.
        Must return object of type ``Move``.

        :type position: Board
        :rtype: Move
        """
        pass

    @staticmethod
    def getUCI():
        """
        Internal method used by ``Interface``
        to read UCI commands from external GUI.

        :rtype: str
        """
        if sys.version_info[0] < 3:
            return raw_input()
        else:
            return input()

    @staticmethod
    def setUCI(command):
        """
        Internal method used by ``Interface``
        to write UCI commands to the console so they
        can be read by external GUI.

        :type command: str
        """
        print(command)

