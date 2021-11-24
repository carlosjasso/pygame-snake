from pathlib import Path
from collections import namedtuple
from pygame import Surface

Position = namedtuple("Position", ["x", "y"])

class Sprite:
    surface : Surface
    position_x : int
    position_y : int
    img_path : Path

    @property
    def position(self) -> Position:
        return Position(self.position_x, self.position_y)

    def __init__(self, img_path : Path):
        self.img_path = img_path
        self.position_x = 0
        self.position_y = 0
