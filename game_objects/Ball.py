""" pure OOP style of the programming. Ball class """
import pygame
import random
from config import config


class Ball:
    """
    Ball in our game -> is a sprite
    """
    def __init__(self, surface, position):
        self.position = position
        self.surface = surface
        self.velocity = [1, 1]
        self.image = None
        self.boom = pygame.mixer.Sound('./static/boom.ogg')
        self.explode = pygame.mixer.Sound('./static/explode.ogg')

    def go(self):
        """
        Start random direction movement
        :return: None
        """
        # if we want to go to the right, we need to decrease x and increase y
        # if we want to go to the left, we need to increase x and decrease y
        h = random.randrange(2, 4)
        v = random.randrange(1, 3)
        if not bool(random.getrandbits(1)):
            h = - h
        self.velocity = [h, -v]
        self.explode.play()

    def change_appearance(self):
        """
        Change drawable image
        :return: None
        """
        pass

    def change_velocity(self, delta):
        """
        Change movement speed of the actor
        :return: None
        """
        self.velocity += delta

    def update_position(self):
        """
        Change the position of the agent to show movement
        :param x: delta on x-axis
        :param y: delta on y-axis
        :return: None
        """
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def draw(self, color):
        pygame.draw.circle(self.surface, color, [int(self.position[0]), int(self.position[1])], 25)

    def is_collided_vertical(self):
        """
        Dissapear on horizontal collision and bounce on vertical
        :return: None
        """
        # bounce of vertical borders -> y-axis-check
        if self.position[1] <= config['globals']['BALL_RADIUS']:
            self.velocity[1] *= -1
        elif self.position[1] >= config['globals']['HEIGHT'] + 1 - config['globals']['BALL_RADIUS']:
            self.velocity[1] *= -1

    def is_collide_horizontal(self, p1, p2):
        # collision with left side
        if (int(self.position[0]) <= config['globals']['BALL_RADIUS'] + config['globals']['PAD_WIDTH']
                and int(self.position[1]) in range(int(p1.position[1] - config['globals']['PAD_HEIGHT'] / 2),
                                                   int(p1.position[1] + config['globals']['PAD_HEIGHT'] / 2))):
            self.boom.play()
            self.velocity[0] *= 1.1
            self.velocity[1] *= 1.1
            self.velocity[0] *= -1
            return
        elif int(self.position[0]) <= config['globals']['BALL_RADIUS'] + config['globals']['PAD_WIDTH']:
            p1.score += 1
            self.position = [int(config['globals']['WIDTH']/2), int(config['globals']['HEIGHT']/2)]
            self.go()
            return

        # collision with right side
        if (int(self.position[0]) >= config['globals']['WIDTH'] + 1 - (
                config['globals']['BALL_RADIUS'] + config['globals']['PAD_WIDTH'])
                and int(self.position[1]) in range(int(p2.position[1] - config['globals']['PAD_HEIGHT'] / 2),
                                                   int(p2.position[1] + config['globals']['PAD_HEIGHT'] / 2))):
            self.boom.play()
            self.velocity[0] *= 1.1
            self.velocity[1] *= 1.1
            self.velocity[0] *= -1
            return
        elif int(self.position[0]) >= config['globals']['WIDTH'] + 1 - (
                config['globals']['BALL_RADIUS'] + config['globals']['PAD_WIDTH']):
            p2.score += 1
            self.position = [int(config['globals']['WIDTH']/2), int(config['globals']['HEIGHT']/2)]
            self.go()
            return
