"""
settings.py
-----------
The settings.
"""

class _settings():
    class _window():
        def __init__(self):
            self.caption = "Structure Iced"             # the caption of the window
            self.size = (800, 680)                      # the size of the window
            self.is_fullscreen = False                  # denote if the game is fullscreened
            
   
    def __init__(self):
        self.window = self._window()

settings = _settings()