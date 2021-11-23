from .sprite import Sprite

class Block(Sprite):
    def __init__(self, img_path: str):
        super().__init__(img_path)
    
    def move_up(self):
        self.position_y -= 40
    
    def move_down(self):
        self.position_y += 40
    
    def move_left(self):
        self.position_x -= 40
    
    def move_right(self):
        self.position_x += 40
