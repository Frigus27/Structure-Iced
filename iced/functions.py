"""
functions.py
------------
Define and implement the game functions that are needed.

For more, see the documentation.
"""

from iced.room import Room, RoomManager
from iced.world import World

def null_function():
    """Just to be a function value means nothing"""

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
