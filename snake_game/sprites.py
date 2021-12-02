from pathlib import Path
from typing import NamedTuple
import pygame
from pygame import Surface
from configuration import WindowSize
from models.enum import SnakeDirection

class Position(NamedTuple):
    X : int
    Y : int

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
    
    def touches_boundry(self, field : WindowSize, direction : SnakeDirection) -> bool:
        match direction:
            case SnakeDirection.UP: return self._touches_top_boundry()
            case SnakeDirection.DOWN: return self._touches_bottom_boundry(field)
            case SnakeDirection.LEFT: return self._touches_left_boundry()
            case SnakeDirection.RIGHT: return self._touches_right_boundry(field)
    
    def _touches_top_boundry(self) -> bool:
        return self._position_y - self.surface.get_height() < 0
    
    def _touches_bottom_boundry(self, field : WindowSize) -> bool:
        return self._position_y + self.surface.get_height() >= field.HEIGHT
    
    def _touches_left_boundry(self) -> bool:
        return self._position_x - self.surface.get_width() < 0

    def _touches_right_boundry(self, field : WindowSize) -> bool:
        return self._position_x + self.surface.get_width() >= field.WIDTH
