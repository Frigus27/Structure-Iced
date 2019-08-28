"""
room.py
-------
A room of a game.

A room in Structure Iced is a plae where the instances
act.

For more, see the documentation.
"""

from iced.instance import Instance, NULL_INSTANCE

def null_function():
    """Just to be a function value means nothing"""

class Room():
    """The room class"""
    def __init__(self):
        self.instance_container = [NULL_INSTANCE]
        self.creation_function = null_function
        self.created = False

    def creation_code(self, creation_function):
        """Set the creation code by sending the function"""
        self.creation_function = creation_function
    
    def add_instance(self, new_instance: Instance):
        """Add an instance to this room"""
        self.instance_container.append(new_instance)

    def loop(self):
        """Do every step when being in the game loop"""
        # create the room
        if not self.created:
            self.creation_function()
            
        # show the instances and do their loops or create
        for i in self.instance_container:
            if not self.created:
                i.containing_game_object.on_create()
            self.created = True
            i.show()
            i.containing_game_object.loop()

class RoomManager():
    """The manager of all the rooms"""

    managing_rooms = { }

    @classmethod
    def add(cls, new_room: Room):
        """
        Add a room to the manager, in order that it
        can be in control. 
        """
        cls.managing_rooms[new_room] = new_room

    @classmethod
    def is_room_exist(cls, room_to_query: Room) -> bool:
        """
        Return whether the room is exits.
        """
        temp = cls.managing_rooms.get(room_to_query, 0)
        return bool(temp) # pylint commanded me for it
    