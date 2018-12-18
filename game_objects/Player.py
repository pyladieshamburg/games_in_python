""" module defining paddle """
import pygame
from config import config


class Paddle:
    def __init__(self, surface, position):
        self.position = position
        self.surface = surface
        self.velocity = 0
        self.image = None
        self.score = 0

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
        # clamp on upper and lower bounds
        new_pos = self.position[1] + self.velocity
        # TODO: proper centering on borders
        if new_pos >= (config['globals']['HEIGHT'] - int(config['globals']['PAD_HEIGHT'] / 2)
                       or new_pos <= int(config['globals']['PAD_HEIGHT'] / 2)):
            pass
        else:
            self.position[1] = new_pos

    def draw(self, color, polygon_coordinates):
        pygame.draw.polygon(self.surface,
                            color,
                            polygon_coordinates,
                            0)

