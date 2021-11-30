from pathlib import Path
import pygame
from pygame import Surface
from .types.sprite_position import Position

class Sprite:
    surface : Surface
    img_path : Path
    _position_x : int
    _position_y : int

    @property
    def position(self) -> Position:
        return Position(self._position_x, self._position_y)
    
    @position.setter
    def position(self, value : Position):
        self._position_x = value.X
        self._position_y = value.Y

    def __init__(self, img_path : Path):
        self.img_path = img_path
        self._position_x = 0
        self._position_y = 0
        self.surface = pygame.image.load(img_path).convert()
