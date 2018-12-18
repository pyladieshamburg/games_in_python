# define event handlers
import sys
import pygame
from pygame.locals import *

from config import config
from game_objects.Ball import Ball
from game_objects.Player import Paddle
from handlers.input_handler import keydown, keyup


def init(window, width, height, pd_w):
    """
    Add objects to the game. It can be a factory, for now we keep it simple
    :param window: game container
    :param width: int width of the container
    :param height: int height of the container
    :param pd_w: int should be half width of the paddle
    :return: main game objects
    """
    # spawn ball
    ball_initial_position = [int(width/2), int(height/2)]
    ball = Ball(window, ball_initial_position)
    # spawn player-paddles
    # 1st player on left
    paddle1_pos = [pd_w - 1, height / 2]
    paddle1 = Paddle(window, paddle1_pos)
    # 2d player on right
    paddle2_pos = [width + 1 - pd_w, height / 2]
    paddle2 = Paddle(window, paddle2_pos)
    # random ball start
    ball.go()
    # add music
    pygame.mixer.music.load('./static/bckground_music.ogg')

    return ball, paddle1, paddle2


def draw_canvas(canvas):
    """
    Draw function for the game filed, aka canvas
    :param canvas: canvas/window
    :return: None
    """
    canvas.fill(config['colors']['BLACK'])
    # make pretty
    pygame.draw.line(canvas,
                     config['colors']['WHITE'],
                     [config['globals']['WIDTH'] / 2, 0],
                     [config['globals']['WIDTH'] / 2, config['globals']['HEIGHT']], 1)
    pygame.draw.line(canvas,
                     config['colors']['WHITE'],
                     [config['globals']['PAD_WIDTH'], 0],
                     [config['globals']['PAD_WIDTH'], config['globals']['HEIGHT']], 1)
    pygame.draw.line(canvas,
                     config['colors']['WHITE'],
                     [config['globals']['WIDTH'] - config['globals']['PAD_WIDTH'], 0],
                     [config['globals']['WIDTH'] - config['globals']['PAD_WIDTH'], config['globals']['HEIGHT']], 1)
    pygame.draw.circle(canvas,
                       config['colors']['WHITE'],
                       [config['globals']['WIDTH'] // 2, config['globals']['HEIGHT'] // 2], 70, 1)


def draw(canvas, ball, paddle1, paddle2):
    """
    Render new game snapshot
    :param canvas: our screen
    :param ball: ball game object
    :param paddle1: player 1 object
    :param paddle2: player 2 object
    :return: None
    """
    # make background
    draw_canvas(canvas)

    # draw paddles and ball
    ball.draw(config['colors']['RED'])
    pad_h_w = int(config['globals']['PAD_WIDTH'] / 2)
    pad_h_h = int(config['globals']['PAD_HEIGHT'] / 2)
    p1_ccordinates = [[paddle1.position[0] - pad_h_w, paddle1.position[1] - pad_h_h],
                      [paddle1.position[0] - pad_h_w, paddle1.position[1] + pad_h_h],
                      [paddle1.position[0] + pad_h_w, paddle1.position[1] + pad_h_h],
                      [paddle1.position[0] + pad_h_w, paddle1.position[1] - pad_h_h]]
    paddle1.draw(config['colors']['GREEN'], p1_ccordinates)
    p2_coordinates = [[paddle2.position[0] - pad_h_w, paddle2.position[1] - pad_h_h],
                      [paddle2.position[0] - pad_h_w, paddle2.position[1] + pad_h_h],
                      [paddle2.position[0] + pad_h_w, paddle2.position[1] + pad_h_h],
                      [paddle2.position[0] + pad_h_w, paddle2.position[1] - pad_h_h]]
    paddle2.draw(config['colors']['WHITE'], p2_coordinates)

    # scores
    myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    label1 = myfont1.render("Score "+ str(paddle2.score), 1, (255, 255, 0))
    canvas.blit(label1, (50, 20))

    myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    label2 = myfont2.render("Score "+str(paddle1.score), 1, (255, 255, 0))
    canvas.blit(label2, (470, 20))


def update(ball, paddle1, paddle2):
    """
    Persist changes onto game state
    :param ball: ball game object
    :param paddle1: player 1 object
    :param paddle2: player 2 object
    :return:
    """
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keydown(event, paddle2, paddle1)
        elif event.type == KEYUP:
            keyup(event, paddle2, paddle1)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    ball.update_position()
    paddle1.update_position()
    paddle2.update_position()
    # check for general collision
    ball.is_collided_vertical()
    # check for paddle collision 1 and 2
    ball.is_collide_horizontal(paddle1, paddle2)

