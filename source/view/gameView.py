import pygame

# a view for the game
class GameView:

    # initializes the game view
    def __init__(self, name, model, columns, rows):
        self.model = model
        self.title = name + "'s Tetris Game"
        self.display_width = (columns * 35) + 150
        self.display_height = rows * 35
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        self.gameDisplay.fill((0,0,0))
        pygame.display.set_caption(self.title)
        self.columns = columns
        self.rows = rows

    # renders everything on the game board
    def render(self):
        pygame.display.update()

