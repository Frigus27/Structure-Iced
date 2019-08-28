from iced.room import Room, RoomManager
from iced.system import System
from iced.game_object import Object
from iced.instance import Instance
from pygame.surface import Surface

def myCreationCode():
    System.screen.fill((230, 230, 230))


class MyObject(Object):
    def loop(self):
        self.pos_x += 1
        self.pos_y += 1

myObj = MyObject()
myObj.set_image_by_surface(Surface((200, 100)))
inst = Instance()
inst.create(myObj, 0, 0)

MyRoom = Room()
MyRoom.creation_code(myCreationCode)
MyRoom.add_instance(inst)

RoomManager.add(MyRoom)