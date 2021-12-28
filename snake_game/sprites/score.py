import pygame
from pygame.font import Font
from sprites import Sprite
from data.types import Color, WindowSize, SpritePosition

class Score(Sprite):
    _score : int
    _font : Font
    _field : WindowSize

    @property
    def font_color(self):
        return Color(255, 255, 255) # HEX color #ffffff

    def __init__(self, window_size : WindowSize) -> None:
        super().__init__(None)
        self._field = window_size
        self._score = 0
        self._font = pygame.font.SysFont("arial", 30)
        self._update_surface()

    def _update_surface(self) -> None:
        self.surface = self._font.render(f"Score: {self._score}", True, self.font_color)
        self.position = SpritePosition(
            X = self._field.WIDTH - self.surface.get_width() - 10,
            Y = 10
        )

    def increase(self):
        self._score += 1
        self._update_surface()
