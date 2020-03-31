# class for configuration variables
import math
import pygame
pygame.init()

class Configs:
    columns = 10
    rows = 20
    blockSize = 30
    name = "Brit"
    gameboardWidth = blockSize * columns
    sidebarBlockSize = blockSize / 2
    sidebarWidth = blockSize * 3 + math.floor(sidebarBlockSize)
    fps = 30

    tetrominoes = [
        #LINE-SHAPE
        [
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0]
            ],
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0]
            ],
            [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0]
            ]
        ],
        # MIRRORED-L
        [
            [
                [2, 0, 0, 0],
                [2, 2, 2, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 2, 2, 0],
                [0, 2, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0],
                [2, 2, 2, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 2, 0, 0],
                [0, 2, 0, 0],
                [2, 2, 0, 0],
                [0, 0, 0, 0]
            ]
        ],
        # L-SHAPE
        [
            [
                [0, 0, 3, 0],
                [3, 3, 3, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 3, 0, 0],
                [0, 3, 0, 0],
                [0, 3, 3, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0],
                [3, 3, 3, 0],
                [3, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [3, 3, 0, 0],
                [0, 3, 0, 0],
                [0, 3, 0, 0],
                [0, 0, 0, 0]
            ]
        ],
        # SQUARE-SHAPE
        [
            [
                [0, 4, 4, 0],
                [0, 4, 4, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 4, 4, 0],
                [0, 4, 4, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 4, 4, 0],
                [0, 4, 4, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 4, 4, 0],
                [0, 4, 4, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
        ],
        # S-SHAPE
        [
            [
                [0, 5, 5, 0],
                [5, 5, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 5, 0, 0],
                [0, 5, 5, 0],
                [0, 0, 5, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0],
                [0, 5, 5, 0],
                [5, 5, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [5, 0, 0, 0],
                [5, 5, 0, 0],
                [0, 5, 0, 0],
                [0, 0, 0, 0]
            ]
        ],
        # T-SHAPE
        [
            [
                [0, 6, 0, 0],
                [6, 6, 6, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 6, 0, 0],
                [0, 6, 6, 0],
                [0, 6, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0],
                [6, 6, 6, 0],
                [0, 6, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 6, 0, 0],
                [6, 6, 0, 0],
                [0, 6, 0, 0],
                [0, 0, 0, 0]
            ]
        ],
        # Z-SHAPE
        [
            [
                [7, 7, 0, 0],
                [0, 7, 7, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 7, 0],
                [0, 7, 7, 0],
                [0, 7, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0],
                [7, 7, 0, 0],
                [0, 7, 7, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 7, 0, 0],
                [7, 7, 0, 0],
                [7, 0, 0, 0],
                [0, 0, 0, 0]
            ]
        ]
    ]

class UIVariables:
    fontBold = pygame.font.Font("./utils/fonts/OpenSans-Bold.ttf", math.floor(Configs.blockSize * 1.5))
    fontTitle = pygame.font.Font("./utils/fonts/OpenSans-Bold.ttf", math.floor(Configs.sidebarBlockSize * 1.5))
    fontReg = pygame.font.Font("./utils/fonts/OpenSans-Regular.ttf", math.floor(Configs.sidebarBlockSize))
    fontLight = pygame.font.Font("./utils/fonts/OpenSans-Light.ttf", math.floor(Configs.sidebarBlockSize))

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
    # LIGHT GRAY
    lightGray = (211, 211, 211)
    # SIDEBAR COLOR
    sidebarColor = (255, 255, 255)
