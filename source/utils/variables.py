# class for configuration variables
import math

class Configs:
    columns = 10
    rows = 20
    blockSize = 35
    name = "Brit"
    sidebarBlockSize = blockSize / 2
    sidebarWidth = blockSize * 3 + math.floor(sidebarBlockSize)

class UIVariables:
    # # Tetriminoe colors
    # # LINE-SHAPE
    # cyan = (69, 206, 204)
    # # MIRRORED-L
    # blue = (64, 111, 249)
    # # L-SHAPE
    # orange = (253, 189, 53)
    # # SQUARE-SHAPE
    # yellow = (246, 227, 90)
    # S-SHAPE
    # green = (98, 190, 68)
    # # T-SHAPE
    # pink = (242, 64, 235)
    # # Z-SHAPE
    # red = (225, 13, 27)
    tetrominoColors = [
        (69, 206, 204), # LINE-SHAPE - cyan
        (64, 111, 249), # MIRRORED-L - blue
        (253, 189, 53), # L-SHAPE - orange
        (246, 227, 90), # SQUARE-SHAPE - yellow
        (98, 190, 68) , # S-SHAPE - green
        (242, 64, 235), # T-SHAPE - pink
        (225, 13, 27), # Z-SHAPE -red
    ]
    # GRAY TILE
    gray = (26, 26, 26)  # rgb(26, 26, 26)
    # SIDEBAR COLOR
    sidebarColor = (255, 255, 255)
