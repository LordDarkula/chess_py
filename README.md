# chess_py
Copyright © 2016 Aubhro Sengupta. All rights reserved.

#License
MIT

<br />8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
<br />7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
<br />6 ║… … … … … … … …
<br />5 ║… … … … … … … …
<br />4 ║… … … … … … … …
<br />3 ║… … … … … … … …
<br />2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
<br />1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
<br />--╚═══════════════
<br />——-a b c d e f g h

## Introduction

Chess_py is an open source chess client and framework written in python. Can create chess matches and provide players with data regarding current position, possible moves and eventual result of the game. External players (either computer or human) are required to play. Works in both Python2 and Python3.

##Installation

To use as a standalone chess client, download or clone, navigate inside chess_py directory, and type the following.
######Note: Works on Python 2 and 3
```bash
python main.py
```
To use as an importable framework in your own python code, you can install manually or using pip.
#####To install manually, download or clone, chess_py directory, and type the following.
```bash
python setup.py install
```
#####Or use pip
```bash
pip install chess_py
```

## Great! How do you use it?

Chess_py has the capability of creating games between players, either human (algebraic notatioon input through console), or AI (through method generate_move(position))
######Note: color.white is defined to be True and color.black is defined to be False in color.py
```python
# Set up
from chess_py import Color, Player, Game, Color, Board, Move

# Creates color objects to initialize players with.
white_color = Color.init_white()
black_color = Color.init_black()
```
If you want to set up a game with two humans, use Player class to initialize a white and a black human.Player objects.
```python
# Creates a game with human players playing white and black
new_game = Game(Player(white_color), Player(black_color))

# Starts game and stores result
# Result is of type integer 
# 1 - White wins
# 0.5 - Draw
# 0 - Black Wins
result = new_game.play()
```
To use a custom player with chess_py, the player must be a python class with a generate_move() method.
```python
# Creates a game with a human player playing white and a separate software playing black
new_game = Game(human.Player(color_white), your_class(color_black))
result = new_game.play()

# In your_class . . . 
class your_class:
    def __init__(self, color):
      # color parameter can be accessed in several different ways
      
      self.color = color
      
      # color_string is either "white" or "black"
      color_string = color.string
      # color_bool is True if color is white, or False if color is black
      color_bool = color.color
      # Your code
    
    def generate_move(self, position):
      # position parameter is an object of type Board
      # Must return a list of objects of type Move
      moves = []
      
      # Move must be initialized with parameters location, piece, status
      # Optional parameters are start_rank (y coordinate from 1 to 7), 
      #start_file (x coordinate from 1 to 7), string, and promoted_to_piece 
      #(one of 6 objects of subclass Piece)
      # Here is an example of the move e4
      my_move = Move(Location(3, 4), position.piece_at_square(Location(1, 4)), 
      # notation_const.MOVEMENT)
      # Notice a couple things:
      # Location is initialized with rank (y coordinate from 1 to 7) first, 
      # then file (x coordinate from 1 to 7)
      # Status is a constant from notation_const 
      # Other constants include CAPTURE, PROMOTE, EN_PASSANT, etc.
      
      # All of that looks tedious. What if I just have a string storing the move in 
      # algebraic notation ie. Nf3 ?
      # Then do the following
      my_move = to_move(my_algebraic_notation_move_stored_as _string)
      # If your_class wanted to move e4
      return to_move("e4")
      
      # This works for any move written in algebraic notation
      return to_move("Nxf3")
      
      # Or even
      return to_move("e8=Q)
      
      # More helpful stuff . . .
      
      # Returns list of all possible moves
      possible = position.all_possible_moves(self.color)
      
      # So if I wanted to return the pawn move that ended on e4 using all_possible_moves . . .
      for move in possible:
        if move.location.equals(Location(3, 4)) and \
            move.piece.equals(position.piece_at_square(Location(1, 4)):
            return move
        # Basically all data types built in to chess_py have an equals()
        # All of them work as you would expect except for the piece equals() method
        # They only compare color of the piece and type,  but not lacation
        # piece_at_square() in Board returns the piece at a certain Location
      
      # Gets my king
      my_king = position.get_king(self.color)
      
      # Returns bool stating if my king is in check
      my_king.in_check(position)
      
      # Your code
      return moves
```
That's it for now! More will be coming shortly.
