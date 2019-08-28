"""
game_object.py
--------------
The implement of the objects in the game.

The game object is the minimum unit to define a interactive
object in a game, e.g. a block, a road, a character, etc.

In Structure Iced, you can easily define an object by
simply inherit the class game_object. A game object
requires the arguments in the following text:

1. An image (which will be showed when game begins)
2. A creation function (To note what the function should do
                        when it is being created)
3. A loop function (To note what the function should do
                    every game loop)
4. A destroying function (The one when it is being
                          destroyed)

For more, see the documentation.
"""

import pygame

class Object():
    """The game object"""

    def __init__(self):
        self.image = 0
        self.image_surface = 0

    def set_image_by_filename(self, new_image_filename: str):
        """To set the image by filename and path"""
        self.image = pygame.image.load(new_image_filename)
        self.image_surface = self.image.convert()

    def set_image_by_surface(self, new_image_surface: pygame.surface.Surface):
        """To set the image by the surface you've created"""
        self.image = 0
        self.image_surface = new_image_surface

    def on_create(self):
        """(to be implied) the function executes when created"""
        raise NotImplementedError

    def loop(self):
        """(to be implied) the function executes every game loop"""
        raise NotImplementedError

    def on_destroy(self):
        """(to be implied) the function executes when destroyed"""
        raise NotImplementedError