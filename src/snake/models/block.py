from pathlib import Path
from .sprite import Sprite

class Block(Sprite):
    def __init__(self, img_path: Path):
        super().__init__(img_path)
    
    def move_up(self):
        self._position_y -= self.surface.get_height()
    
    def move_down(self):
        self._position_y += self.surface.get_height()
    
    def move_left(self):
        self._position_x -= self.surface.get_width()
    
    def move_right(self):
        self._position_x += self.surface.get_width()
