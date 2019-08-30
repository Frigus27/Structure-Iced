"""
functions.py
------------
Define and implement the game functions that are needed.

For more, see the documentation.
"""
import pygame
from pygame.locals import *

from iced.room import Room, RoomManager
from iced.world import World
from iced.game_object import Object
from iced.instance import Instance
from iced.system import System
from iced.settings import settings

def null_function():
    """Just to be a function value means nothing"""

def offset_rect(pos_x: int, pos_y: int, rect: pygame.Rect):
    """offset the rect by the position sent"""
    return pygame.Rect(pos_x, pos_y, pos_x + rect.width, pos_y + rect.height)

# About the game
def set_caption(new_caption: str):
    """Set the caption of the game"""
    settings.window.caption = new_caption

# About the easy test
def is_point_in_rect(pos_x: int, pos_y: int, rect: pygame.Rect):
    """detect if the point (pos_x, pos_y) is in rect"""
    return (rect.x <= pos_x and pos_x <= rect.x + rect.width) and (rect.y <= pos_y and pos_y <= rect.y + rect.width)

# About the rooms
def room_goto(new_room: Room):
    """
    Go to the room if the room is being managed;
    else raise an error
    """
    if RoomManager.is_room_exist(new_room):
        World.current_room = new_room
    else:
        raise ValueError
    
# About the mouse
def is_mouse_left_down(the_object: Object):
    """returns if the left key of the mouse is on the instance of the object"""
    if System.mouse_state[0] == 1:
        rect = offset_rect(the_object.InstanceVariables.pos_x, the_object.InstanceVariables.pos_y, the_object.image_surface.get_rect())
        if is_point_in_rect(System.mouse_position[0], System.mouse_position[1], rect):
            return True
    return False

def is_mouse_right_down(the_object: Object):
    """returns if the right key of the mouse is on the instance of the object"""
    if System.mouse_state[2] == 1:
        rect = offset_rect(the_object.InstanceVariables.pos_x, the_object.InstanceVariables.pos_y, the_object.image_surface.get_rect())
        if is_point_in_rect(System.mouse_position[0], System.mouse_position[1], rect):
            return True
    return False

# About the keyboard
def is_key_down(key: int):
    """returns if the key on the keyboard is pressed"""
    return System.keyboard_state[key]
