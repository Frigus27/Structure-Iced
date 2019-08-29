"""
functions.py
------------
Define and implement the game functions that are needed.

For more, see the documentation.
"""
import pygame

from iced.room import Room, RoomManager
from iced.world import World

def null_function():
    """Just to be a function value means nothing"""

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
def mouse_left_down_on():
    """About the mouse"""
    # TODO: do with it
