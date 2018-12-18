""" input handlers: movement and others """
from pygame.locals import *


def keydown(event, game_obj1, game_obj2):
    """
    Change the velocity of a game obj by pressing up or down arrows
    :param event: game event loop
    :param game_objX: gam object with velocity attribute
    :return: None
    """
    if event.key == K_UP:
        game_obj1.velocity = -8
    elif event.key == K_DOWN:
        game_obj1.velocity = 8
    elif event.key == K_w:
        game_obj2.velocity = -8
    elif event.key == K_s:
        game_obj2.velocity = 8


def keyup(event, game_obj1, game_obj2):
    if event.key in (K_w, K_s):
        game_obj2.velocity = 0
    elif event.key in (K_UP, K_DOWN):
        game_obj1.velocity = 0
