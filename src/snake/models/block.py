from pathlib import Path

from pygame import surface
import pygame
from .sprite import Sprite

class Block(Sprite):
    def __init__(self, img_path: Path):
        super().__init__(img_path)
        self.surface = pygame.image.load(img_path).convert()
    
    def move_up(self):
        self.position_y -= self.surface.get_height()
    
    def move_down(self):
        self.position_y += self.surface.get_height()
    
    def move_left(self):
        self.position_x -= self.surface.get_width()
    
    def move_right(self):
        self.position_x += self.surface.get_width()
