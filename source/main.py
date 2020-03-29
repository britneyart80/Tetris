import pygame
from source.view.gameView import GameView
from source.model.gameboard import Gameboard
from source.model.sidebar import Sidebar
from source.controller.gameController import GameController
from source.utils.enums.difficulty import Difficulty
from source.utils.variables import Configs

def main():
    columns = Configs.columns
    rows = Configs.rows
    name = Configs.name
    gameboard = Gameboard(Difficulty.BEGINNER, columns, rows)
    sidebar = Sidebar()
    gameView = GameView(name, gameboard, sidebar, columns, rows)
    gameController = GameController(gameboard, gameView, sidebar, columns, rows)
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
