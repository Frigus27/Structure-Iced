"""
instance.py
-----------
The implement of a game instance in the game.

A game instance is an instance of a game object, like a
variable of a class in Python. A game instance is an
independent copy of the object, and that means every
instances should not make a difference on the code
by game functions themselves. And also, it is what the
player actually see and interact with in the game.

To create an instance, you should send the object you wish
to be instantiated and the position x and y.

For more, see the documentation.
"""

from iced.game_object import Object
from iced.system import System

import pygame

class Instance():
    """
    Instance: the implement of instances.
    """
    def __init__(self):
        self.containing_game_object = Object()
        self.pos_x = 0
        self.pos_y = 0

    def create(self, new_game_object: Object, new_x: int, new_y: int):
        """create the instance from an object"""
        self.containing_game_object = new_game_object
        self.containing_game_object.update_instance_pos(new_x, new_y)
        self.pos_x, self.pos_y = self.containing_game_object.get_instance_pos()

    def show(self):
        """show the instance"""
        System.screen.blit(self.containing_game_object.image_surface, (self.pos_x, self.pos_y))

    def loop(self):
        """the loop"""
        self.show()
        
        self.containing_game_object.loop()
        self.containing_game_object.instance_x += 1
        self.pos_x, self.pos_y = self.containing_game_object.get_instance_pos()

    def get_pos(self) -> (int, int):
        """get the position"""
        return (self.pos_x, self.pos_y)

NULL_INSTANCE = Instance()
NULL_INSTANCE.create(Object(), 32, 32)
