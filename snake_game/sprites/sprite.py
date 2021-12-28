from pathlib import Path
import pygame
from pygame import Surface
from data.types import SpritePosition

class Sprite:
    surface : Surface
    img_path : Path
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
        self.img_path = img_path
        self._position_x = 0
        self._position_y = 0
        self.surface = pygame.image.load(img_path).convert() \
            if img_path != None else None
