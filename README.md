# chess_py

#8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
#7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
#6 ║… … … … … … … …
#5 ║… … … … … … … …
#4 ║… … … … … … … …
#3 ║… … … … … … … …
#2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
#1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
#--╚═══════════════
#——-a b c d e f g h

# Introduction

Chess_py is an open source chess platform written in python. Can create chess matches and provide players with data regarding current position, possible moves and eventual result of the game. External players (either computer or human) are required to play.

#Great! How do you use it?

```python
from chess_py import *

# creates a game with human players playing white and black
new_game = Game(human.Player(color.white), human.player(color.black))
```
