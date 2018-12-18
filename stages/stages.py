import pygame
from config import config
from handlers.initialization import init, draw, update
from handlers.input_handler import keydown, keyup


class States:
    """ define abstract state/screen in-game. Future parent for a state """
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None


class Menu(States):
    """ starter menu state """
    def __init__(self):
        States.__init__(self)
        self.next = 'game'

    def cleanup(self):
        """ finish all game-dependent processes that run on global game level """
        pass

    def startup(self, screen):
        """ start all processes associated with the game """
        pass

    def get_event(self, event):
        """ register user input """
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True

    def update(self, screen):
        """ based on input update objects """
        self.draw(screen)

    def draw(self, screen):
        """ show current state"""
        screen.fill(config['colors']['BLACK'])
        # make pretty
        myfont = pygame.font.SysFont("Comic Sans MS", 20)
        label1 = myfont.render("Ping Pong game".format(), 1, config['colors']['WHITE'])
        screen.blit(label1, (250, 20))  # (y,x)
        player1 = myfont.render("Left Player Movement:", 1, config['colors']['WHITE'])
        screen.blit(player1, (100, 150))
        player1 = myfont.render("W - up", 1, config['colors']['WHITE'])
        screen.blit(player1, (100, 180))
        player1 = myfont.render("S - down", 1, config['colors']['WHITE'])
        screen.blit(player1, (100, 210))
        player2 = myfont.render("Right Player Movement:", 1, config['colors']['WHITE'])
        screen.blit(player2, (400, 150))
        player2 = myfont.render("UP - up", 1, config['colors']['WHITE'])
        screen.blit(player2, (400, 180))
        player2 = myfont.render("DOWN - down", 1, config['colors']['WHITE'])
        screen.blit(player2, (400, 210))


class Game(States):
    """ actual game state """
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'
        self.ball = None
        self.p1 = None
        self.p2 = None

    def cleanup(self):
        """ finish all game-dependent processes that run on global game level """
        pygame.mixer.music.stop()

    def startup(self, screen):
        """ start all processes associated with the game """
        self.ball, self.p1, self.p2 = init(screen,
                            config['globals']['WIDTH'],
                            config['globals']['HEIGHT'],
                            int(config['globals']['PAD_WIDTH'] / 2))
        pygame.mixer.music.play()

    def get_event(self, event):
        """ register user input """
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True
        elif event.type == pygame.KEYDOWN:
            keydown(event, self.p2, self.p1)
        elif event.type == pygame.KEYUP:
            keyup(event, self.p2, self.p1)

    def update(self, screen):
        """ based on input update objects """
        # collect input and update objects
        update(self.ball, self.p1, self.p2)
        self.draw(screen)

    def draw(self, screen):
        """ show current state """
        screen.fill(config['colors']['BLACK'])
        # make pretty
        pygame.draw.line(screen,
                         config['colors']['WHITE'],
                         [config['globals']['WIDTH'] / 2, 0],
                         [config['globals']['WIDTH'] / 2,
                          config['globals']['HEIGHT']], 1)
        pygame.draw.line(screen,
                         config['colors']['WHITE'],
                         [config['globals']['PAD_WIDTH'], 0],
                         [config['globals']['PAD_WIDTH'],
                          config['globals']['HEIGHT']], 1)
        pygame.draw.line(screen,
                         config['colors']['WHITE'],
                         [config['globals']['WIDTH'] - config['globals']['PAD_WIDTH'], 0],
                         [config['globals']['WIDTH'] - config['globals']['PAD_WIDTH'],
                          config['globals']['HEIGHT']], 1)
        pygame.draw.circle(screen,
                           config['colors']['WHITE'],
                           [config['globals']['WIDTH'] // 2,
                            config['globals']['HEIGHT'] // 2], 70, 1)
        draw(screen, self.ball, self.p1, self.p2)


