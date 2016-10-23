from . import algebraic
from .algebraic import Move, Location, converter, notation_const
from .board import Board

__all__ = (['Board', 'color'] + algebraic.__all__)
