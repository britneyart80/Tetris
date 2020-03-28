# enum for determining game difficulty
from enum import Enum

class Tetrominoe(Enum):
    S_SHAPE = "S-SHAPE"
    Z_SHAPE = "Z-SHAPE"
    T_SHAPE = "T-SHAPE"
    L_SHAPE = "L-SHAPE"
    LINE_SHAPE = "LINE_SHAPE"
    MIRRORED_L = "MIRRORED-L"
    SQUARE = "SQUARE_SHAPE"