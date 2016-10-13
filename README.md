# chess_py

[![Build Status](https://travis-ci.org/LordDarkula/chess_py.svg?branch=master)](https://travis-ci.org/LordDarkula/chess_py)
[![Code Climate](https://codeclimate.com/github/LordDarkula/chess_py/badges/gpa.svg)](https://codeclimate.com/github/LordDarkula/chess_py)
[![PyPI version](https://badge.fury.io/py/chess_py.svg)](https://pypi.python.org/pypi/chess_py)
[![Python27](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/download/releases/2.7/)
[![Python35](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-350/)
[![License](https://img.shields.io/cocoapods/l/EasyQL.svg?style=flat)](https://github.com/LordDarkula/chess_py/blob/master/LICENSE)
[![Twitter](https://img.shields.io/badge/twitter-@LordDarkula-blue.svg?style=flat)](http://twitter.com/LordDarkula)
```

8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
6 ║… … … … … … … …
5 ║… … … … … … … …
4 ║… … … … … … … …
3 ║… … … … … … … …
2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
--╚═══════════════
——-a b c d e f g h
```

## License
chess_py is available under the MIT license. See the LICENSE file for more info.
Copyright © 2016 Aubhro Sengupta. All rights reserved.

## Introduction

Chess_py is an open source chess client and framework written in python. Can create chess matches and provide players with data regarding current position, possible moves and eventual result of the game. UCI integration in progress.

## Installation

To use as a immediately start up a game between two human players in the console, navigate inside the root directory of the package and run main.py. 

```bash
python main.py
```

To install package  

### pip
```bash
pip install chess_py
```

### Or manually
```bash
python setup.py install
```
## Documentation

View complete technical documentation [here](http://lorddarkula.github.io/chess_py).

## Great! How do you use it? (An Example)

Chess_py has the capability of creating games between players, either human, or AI 

```python
import chess_py
from chess_py import Game, Human, color

""" Creates a Game with 2 humans. 
When run, this will open the console,"""
new_game = Game(Human(color.white), Human(color.black))

""" After game is completed, outcome will be stored in result.
The integer result will be one of three values. 
white wins - 0, black wins - 1, draw - 0.5 """
result = new_game.play()
```

To build a chess engine on with chess_py, inherit Player and implement generate_move() 

```python

# Engine which plays the move with the highest immediate material advantage
class My_engine:
    def __init__(self, color):
    
      # Creates piece value scheme to specify value of each piece.
      self.piece_values = chess_py.Piece_values.init_manual(PAWN_VALUE=1,
                                                            KNIGHT_VALUE=3,
                                                            BISHOP_VALUE=3,
                                                            ROOK_VALUE=5,
                                                            QUEEN_VALUE=9)
      
      # Super call makes color a global
      super(Human, self).__init__(input_color)
    
    def generate_move(self, position):
      # position parameter is an object of type Board
        
      # Finds all possible moves I can play.
      moves = position.all_possible_moves(self.color)
      
      # Initalizes best move and advantage after it has been played to dummy values.
      best_move = None
      best_move_advantage = -99
      
      # Loops through possible moves
      for move in move:
        """ advantage_as_result(move, piece_values) finds numerical advantage
        as specified by piece value scheme above. Returns negative values for
        positions of disadvantage. Returns +/-99 for checkmate. """
        advantage = position.advantage_as_result(move, self.piece_values)
        
        # If this move is better than best move, it is the best move.
        if advantage >= best_move_advantage:
            best_move = move
            best_move_advantage = advantage
      
      return move

# If file is run as script, a Game is set up between My_engine and Human and result is printed.
if __name__ == "__main__":
    new_game = My_engine(Human(color.white), Human(color.black))
    
    # white wins - 0, black wins - 1, draw - 0.5 
    print("Result: ", new_game.play())
```

