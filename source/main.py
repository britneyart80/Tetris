import pygame
from source.view.gameView import GameView
from source.model.game import Game
from source.controller.gameController import GameController
from source.utils.enums.difficulty import Difficulty

def main():
    columns = 10
    rows = 20
    name = "Brit"
    game = Game(Difficulty.BEGINNER, columns, rows)
    gameView = GameView(name, game, columns, rows)
    gameController = GameController(game, gameView, columns, rows)
    while True:
        gameController.playGame()

def start_game():
    pygame.mixer.pre_init(channels=32)
    pygame.init()
    main()
    pygame.quit()
    pygame.mixer.quit()


if __name__ == "__main__":
    start_game()
