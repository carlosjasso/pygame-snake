from pathlib import Path
from sprites import Sprite
from utils.types import SpritePosition, WindowSize

class Apple(Sprite):
    _field : WindowSize

    def __init__(self, window_size : WindowSize, img_path : Path) -> None:
        super().__init__(img_path)
        self._field = window_size
        self.position = SpritePosition(0, 0)
