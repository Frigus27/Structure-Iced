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
from iced.world import World
from iced.system import System
from iced.room import Room
from iced.functions import *

class Game(object):
    """The main game object"""

    def initialize(self, start_room: Room):
        """Initialize the pygame and the screen"""
        pygame.init()
        System.screen = pygame.display.set_mode(settings.window.size, settings.window.is_fullscreen)
        pygame.display.set_caption(settings.window.caption)
        room_goto(start_room)

    def loop(self):
        """The main game loop operator"""
        # update the caption
        pygame.display.set_caption(settings.window.caption)
        while True:
            # erase the screen
            World.current_room.show_background()

            # TODO: event handler
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                System.mouse_position = pygame.mouse.get_pos()
                System.mouse_state = pygame.mouse.get_pressed()
            
            # loop the room
            World.current_room.loop()
            # update the display
            pygame.display.update()
            # tick
            System.clock.tick(60)

    def quit(self):
        """The code when quit the game"""
        exit()

    def main(self, start_room: Room):
        """The only callable function to start a game"""
        self.initialize(start_room)
        self.loop()
