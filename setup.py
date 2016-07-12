#!/usr/bin/env python

from distutils.core import setup

setup(name='chess_py',
      version='1.0',
      description='Python chess client',
      author='Aubhro Sengupta',
      author_email='aubhrosengupta@gmail.com',
      url='https://github.com/LordDarkula/chess_py',
      packages=['chess_py', 'chess_py.core', 'chess_py.core.algebraic', 'chess_py.game', 'chess_py.pieces',
                'chess_py.players'],
      )
