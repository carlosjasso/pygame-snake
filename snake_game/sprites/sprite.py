from pathlib import Path
import pygame
from pygame import Surface
from utils.types import SpritePosition

class Sprite:
    _surface : Surface
    _position_x : int
    _position_y : int

    @property
    def position(self) -> SpritePosition:
        return SpritePosition(self._position_x, self._position_y)

    @position.setter
    def position(self, value : SpritePosition):
        self._position_x = value.X
        self._position_y = value.Y

    def __init__(self, img_path : Path):
        self._position_x = 0
        self._position_y = 0
        self._surface = pygame.image.load(img_path).convert() \
            if img_path != None else None

    @property
    def width(self) -> int:
        return self._surface.get_width()

    @property
    def height(self) -> int:
        return self._surface.get_height()

    @property
    def surface(self) -> Surface:
        return self._surface

    @surface.setter
    def surface(self, value : Surface):
        self._surface = value
