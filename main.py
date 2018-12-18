import pygame
import os
print(os.getcwd())
from config import config
from handlers.initialization import init, draw, update


if __name__ == '__main__':
   # the engine warm up
    pygame.init()
    clock = pygame.time.Clock()

    # the speed of the visualization/logic
    fps = pygame.time.Clock()

    # creating a container
    window = pygame.display.set_mode((config['globals']['WIDTH'],
                                      config['globals']['HEIGHT']), 0, 32)

    # some additional stuff for the rendered window
    pygame.display.set_caption('PingPong. PyLadies Edition')

    # initialize game objects
    ball, p1, p2 = init(window,
                        config['globals']['WIDTH'],
                        config['globals']['HEIGHT'],
                        int(config['globals']['PAD_WIDTH'] / 2))
    pygame.mixer.music.play()

    # game loop
    while True:
        # refresh rendering
        draw(window, ball, p1, p2)
        # collect input and update objects
        update(ball, p1, p2)
        pygame.display.update()
        fps.tick(60)
