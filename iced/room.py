"""
room.py
-------
A room of a game.

A room in Structure Iced is a plae where the instances
act.

For more, see the documentation.
"""

from iced.instance import Instance
from iced.functions import null_function

class room(object):
    def __init__(self):
        self.instance_container = []
        self.creation_function = null_function
        self.created = False

    def creation_code(self, creation_function):
        self.creation_function = creation_function
    
    # add an instance to the room
    def add_instance(self, new_instance: Instance):
        self.instance_container.append(new_instance)

    # the loop of all the instances
    def loop(self):
        # create the room
        if not self.created:
            self.creation_function()
            self.created = True
        
        # show the instances
        for i in self.instance_container:
            i.show()