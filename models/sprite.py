from collections import namedtuple
from pygame import Surface

Position = namedtuple("Position", ["x", "y"])

class Sprite:
    def __init__(self, name : str, path : str) -> None:
        self.name = name
        self.path = path
        self.position = Position(x = 0, y = 0)
        self.surface : Surface = None
