# chess_py

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

Chess_py is an open source chess platform written in python. Can create chess matches and provide players with data regarding current position, possible moves and eventual result of the game. External players (either computer or human) are required to play.

## Great! How do you use it?

Chess_py must be imported and a game object must be created. The game object requires 2 parameters for the players. These players can be human (from the included human.player class) or artificial intelligence of some kind. Basic set up required is shown below.

######Note: color.white is defined to be True and color.black is defined to be False in color.py
```python
# Set up
from chess_py import *

# Creates color objects to initialize players with.
white_color = color.Color(color.white)
black_color = color.Color(color.black)
```
If you want to set up a game with two humans, use human.Player class to initialize a white and a black human.Player objects.


```python
# Creates a game with human players playing white and black
new_game = Game(human.Player(white_color), human.player(black_color))
new_game.start()
```

To use a custom artificial intelligence with chess_py, the artificial intelligence must be a python class with a generate_move() method.
```python
# Creates a game with a human player playing white and a separate software playing black
new_game = Game(human.Player(color_white), your_class(color_black))
new_game.start()

# In your_class . . . 
class your_class:
    def __init__(self, color):
      # color parameter stores boolean True for white and False for black.
      # Your code
    
    def generate_move(self, position):
      # position parameter is an object of type board.Board
      # Must return a list of objects of type algebraaic.Move
      moves = []
      
      # Your code
      return moves
```

Board.board stores the chess board. Initialization is shown below.
```python
# Initializes chess board with default starting position.
my_board = board.Board.init_default()
```
######Or
```python
"""
my_list must be a 2-Dimensional 8 by 8 list containing None and/or any of the built in piece classes.
There has be exactly one white king and exactly one black king in my_list.
"""
my_list = [""" Your code here """]
# Initializes chess board with custom position.
my_board = board.Board()
```
So what can this class do?
