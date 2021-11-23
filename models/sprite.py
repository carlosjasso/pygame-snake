from collections import namedtuple
from pygame import Surface

Position = namedtuple("Position", ["x", "y"])

class Sprite:
    surface : Surface
    position_x : int
    position_y : int
    img_path : str

    @property
    def position(self):
        return Position(self.position_x, self.position_y)

    def __init__(self, img_path : str):
        self.img_path = img_path
        self.position_x = 0
        self.position_y = 0
