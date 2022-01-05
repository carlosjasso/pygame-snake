import pygame
from pygame.font import Font
from sprites import Sprite
from utils.types import Color, WindowSize, SpritePosition

class GameOver(Sprite):
    _font : Font
    _field : WindowSize

    @property
    def font_color(self):
        return Color(0, 0, 0) # HEX color #ffffff

    def __init__(self, window_size: WindowSize) -> None:
        super().__init__(None)
        self._field = window_size
        self._font = pygame.font.SysFont("arial", 180, bold=True)
        self.surface = self._font.render("GAME OVER", True, self.font_color)
        self.position = SpritePosition(
            X = (window_size.WIDTH - self.width) / 2,
            Y = (window_size.HEIGHT - self.height) / 2)
