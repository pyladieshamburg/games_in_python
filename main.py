import pygame
from stages.controller import Control


if __name__ == '__main__':
    pygame.init()

    app = Control()
    app.setup_states('menu')

    app.main_game_loop()

    pygame.quit()
