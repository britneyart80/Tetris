import pygame
from source.view.gameView import GameView
from source.model.game import Game
from source.controller.gameController import GameController
from source.utils.enums.difficulty import Difficulty
from source.utils.variables import Configs

def main():
    columns = Configs.columns
    rows = Configs.rows
    name = Configs.name
    blockSize = Configs.blockSize
    gameboard = Game(Difficulty.BEGINNER, columns, rows)
    gameView = GameView(name, gameboard, columns, rows)
    gameController = GameController(gameboard, gameView, columns, rows)
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
