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

    class _InstanceVariables():
        def __init__(self):
            self.pos_x = 0
            self.pos_y = 0

    def __init__(self):
        self.image = 0
        self.image_surface = pygame.surface.Surface((0, 0))
        self.InstanceVariables = _InstanceVariables()

    def set_image_by_filename(self, new_image_filename: str):
        """To set the image by filename and path"""
        self.image = pygame.image.load(new_image_filename)
        self.image_surface = self.image.convert()

    def set_image_by_surface(self, new_image_surface: pygame.surface.Surface):
        """To set the image by the surface you've created"""
        self.image = 0
        self.image_surface = new_image_surface

    def on_create(self):
        """the function executes when created"""

    def loop(self):
        """the function executes every game loop"""

    def on_destroy(self):
        """the function executes when destroyed"""

    def update_instance_pos(self, new_pos_x: int, new_pos_y: int):
        """update the position of the instance of the object"""
        self.InstanceVariables.pos_x = new_pos_x
        self.InstanceVariables.pos_y = new_pos_y

    def get_instance_pos(self):
        """get the position of the instance of the object"""
        return self.InstanceVariables.pos_x, self.InstanceVariables.pos_y
