from pathlib import Path
from data.types.sprite_position import SpritePosition
from sprites import Sprite
from data.enum import SnakeDirection
from data.types import WindowSize

class Block(Sprite):
    def __init__(self, img_path: Path):
        super().__init__(img_path)
    
    #region Move
    def move_up(self):
        self._position_y -= self.surface.get_height()
    
    def move_down(self):
        self._position_y += self.surface.get_height()
    
    def move_left(self):
        self._position_x -= self.surface.get_width()
    
    def move_right(self):
        self._position_x += self.surface.get_width()
    #endregion
    
    #region Touches Boundry
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
    #endregion
    
    def touches_apple(self, apple_position : SpritePosition) -> bool:
        return self.position.X == apple_position.X and self.position.Y == apple_position.Y
