from iced.room import Room, RoomManager
from iced.game_object import Object
from iced.instance import Instance
from pygame.surface import Surface
from iced.settings import settings



class MyObject(Object):
    def __init__(self):
        super().__init__()
        self.k = 0
        self.raising = True
    
    def loop(self):
        if self.raising:
            if self.k < 230:
                self.k += 1
            else:
                self.raising = False
        else:
            if self.k > 0:
                self.k -= 1
            else:
                self.raising = True
        self.image_surface.fill((self.k, self.k, self.k))
        self.instance_x += 1
        self.instance_y += 1
        if self.instance_x >= settings.window.size[0]:
            self.instance_x -= settings.window.size[0] + 200
        if self.instance_y >= settings.window.size[1]:
            self.instance_y -= settings.window.size[1] + 100

myObj = MyObject()
myObj.set_image_by_surface(Surface((200, 100)))
inst = Instance()
inst.create(myObj, 100, 100)

MyRoom = Room()
back = Surface(settings.window.size)
back.fill((230, 230, 230))
MyRoom.set_background(back)
MyRoom.add_instance(inst)

RoomManager.add(MyRoom)