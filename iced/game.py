"""
game.py
-------
The main object of a game.

Use the object to start a game.

For more, see the documentation.
"""

import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, KEYDOWN, KEYUP

from iced.settings import settings

from iced.system import System

class Game(object):
    """The main game object"""

    def initialize(self):
        """Initialize the pygame and the screen"""
        pygame.init()
        System.screen = pygame.display.set_mode(settings.window.size, settings.window.fullscreen)
        pygame.display.set_caption(settings.window.caption)

    def loop(self):
        """The main game loop operator"""
        while True:
            # event handler
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    pass
                elif event.type == MOUSEBUTTONUP:
                    pass
                elif event.type == MOUSEMOTION:
                    pass
                elif event.type == KEYDOWN:
                    pass
                elif event.type == KEYUP:
                    pass

            # update the display
            pygame.display.update()

    def quit(self):
        """The code when quit the game"""
        exit()

    def main(self):
        """The only callable function to start a game"""
        self.initialize()
        self.loop()
