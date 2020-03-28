# enum for determining game difficulty
from enum import Enum

class Difficulty(Enum):
    # slow blocks, easy to work with pieces
    BEGINNER = 1
    # medium speed blocks, medium piece
    INTERMEDIATE = 2
    # fast blocks, bad blocks
    HARD = 3
    # fast blocks, bad blocks
    EXTREME = 4
