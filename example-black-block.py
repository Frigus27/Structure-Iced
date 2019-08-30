"""
An example of Structure Iced.

It will show a moving block on the screen with the
rising and fading color of black. When you pressed
the left mpuse key on it, the block will be filled
with pure black; and when you pressed the right key
on it, it will be filled with pure white. And by
holding the space key, you'll be able to stop the
block.

The example shall show how to use the game structure
Structure Iced. It may be a great example.
"""

# To start a game
from iced.game import Game

# To create a room to include the block
from iced.room import Room, RoomManager

# To create the block as an object
from iced.game_object import Object

# To make an instance of the block
from iced.instance import Instance

# To import the game functions
from iced.functions import *

# To read and edit the settings
from iced.settings import settings

# To create an image of the black block
from pygame.surface import Surface

# To import the values of pygame
from pygame.locals import *

class BlackBlock(Object):
    """The object we defines"""

    # If you want to define a variable you own, then you
    # must override the __init__ function and write the
    # function as following sentences.
    def __init__(self):
        # (Critical) To import the included variable of
        # the base class. If you forget that, it will be
        # really sad.
        super().__init__()
        # Our new variables.
        # Here defines the color value.
        self.color_value = 0
        # This flags if the color is raising or fading.
        self.raising = True
        # This flags if the block is moving
        self.moving = True
    
    def loop(self):
        """
        Here is the loop function. In this function
        you will do everything that controls your
        object (instance) in a game loop.
        """

        # Detect the state of the mouse, and change.
        if is_mouse_left_down(self):
            self.color_value = 0
        if is_mouse_right_down(self):
            self.color_value = 255

        self.moving = True
        # Detect the state of the keyboard, and change.
        if is_key_down(K_SPACE):
            self.moving = False

        # The image controlling code
        if self.raising:
            if self.color_value < 255:
                self.color_value += 1
            else:
                self.raising = False
        else:
            if self.color_value > 0:
                self.color_value -= 1
            else:
                self.raising = True

        # Draw the image on its image. The updating
        # of the screen is not requiring.
        self.image_surface.fill((self.color_value, self.color_value, self.color_value))

        # Now move the object by increasing the position
        # if it is able to move.
        if self.moving:
            self.InstanceVariables.pos_x += 3
            self.InstanceVariables.pos_y += 2

        # If the block has moved outside the screen,
        # then pull it back.
        if self.InstanceVariables.pos_x >= settings.window.size[0]:
            self.InstanceVariables.pos_x -= settings.window.size[0] + 200
        if self.InstanceVariables.pos_y >= settings.window.size[1]:
            self.InstanceVariables.pos_y -= settings.window.size[1] + 100
        

# Create an instance of our black block.
# The steps includes setting the images and create
# an instance my sending the object instance and
# its position.
myObj = BlackBlock()
myObj.set_image_by_surface(Surface((200, 100)))
inst = Instance()
inst.create(myObj, settings.window.size[0] // 2, 100)

# Now create our room.
MyRoom = Room()

# Create a background (filled with white) for the room.
back = Surface(settings.window.size)
back.fill((255, 255, 255))

# Set it the background.
MyRoom.set_background(back)

# Now add the instance of our black block to our room.
MyRoom.add_instance(inst)

# Manage the room. This step is critical because you 
# won't be able to wrap to the room unless you manage it.
RoomManager.add(MyRoom)

# Set our amazing caption of the window.
set_caption("Our colorful black block!")

# Now create our game.
MY_GAME = Game()

# Set our room as the first, then start!
MY_GAME.main(MyRoom)
