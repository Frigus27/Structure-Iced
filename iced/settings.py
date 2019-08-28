# settings.py: the settings of a game
#

class _settings(object) :
    class _window(object) :
        def __init__(self):
            self.caption = "Iced Structure"         # the caption of the window
            self.size = (800, 680)                   # the size of the window
            self.fullscreen = False                 # denote if the game is fullscreened
            
   
    def __init__(self):
        self.window = self._window()

settings = _settings()