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

# Introduction

Chess_py is an open source chess platform written in python. Can create chess matches and provide players with data regarding current position, possible moves and eventual result of the game. External players (either computer or human) are required to play.

#Great! How do you use it?

Chess_py must be imported and a game object should be created. The game object requires 2 parameters for the players. These players can be human (from the included human.player class) or artificial intelligence of some kind. 
```python
from chess_py import *

# Creates a game with human players playing white and black
new_game = Game(human.Player(color.white), human.player(color.black))
new_game.start()
```
To use a custom artificial intelligence with chess_py, the artificial intelligence must be a python class with a generate_move() method.
```python
from chess_py import *

# Creates a game with a human player playing white and a separate software playing black
new_game = Game(human.Player(color.white), your_class(color.black))
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
