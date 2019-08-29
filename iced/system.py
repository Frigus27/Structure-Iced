"""
system.py
--------
The system of a game.

The object "system" saves the critical variables of a
game, which needs to be saved globally and shared. e.g.
the screen object of pygame.

For more, see the documentation.
"""

import pygame

class System():
    """The system object"""
    screen = pygame.surface.Surface((0, 0))
    """The clock"""
    clock = pygame.time.Clock()
    """The position of the mouse"""
    mouse_position = (0, 0)
    """The state of the mouse"""
    mouse_state = (False, False, False)