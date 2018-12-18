import pygame
from config import config
from stages.stages import Game, Menu


class Control:
    """ State controller to switch between "screens" """
    def __init__(self, **settings):
        self.__dict__.update(settings)
        self.done = False
        self.screen = pygame.display.set_mode((config['globals']['WIDTH'],
                                               config['globals']['HEIGHT']),
                                              0, 32)
        pygame.display.set_caption('PingPong. PyLadies Edition')

        self.clock = pygame.time.Clock()
        self.state_dict = {
            'menu': Menu(),
            'game': Game()
        }
        self.state_name = None
        self.state = None
        self.fps = pygame.time.Clock()

    def setup_states(self, start_state):
        """ helper function """
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        """ switch state """
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.screen)
        self.state.previous = previous

    def update(self):
        """ check which state should be used """
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen)

    def event_loop(self):
        """ getting input events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.state.get_event(event)

    def main_game_loop(self):
        """
        Main game loop where getting events and updating happens
        :return:
        """
        while not self.done:
            self.event_loop()
            self.update()
            pygame.display.update()
            self.fps.tick(config['globals']['FPS'])
