from pathlib import Path
from utils.types.sprite_position import SpritePosition
from sprites import Sprite
from utils.enum import SnakeDirection
from utils.types import WindowSize

class Block(Sprite):
    def __init__(self, img_path: Path):
        super().__init__(img_path)

    #region Move
    def move_up(self):
        # self._position_y -= self.height
        self.position = SpritePosition(
            X = self.position.X,
            Y = self.position.Y - self.height
        )

    def move_down(self):
        # self._position_y += self.height
        self.position = SpritePosition(
            X = self.position.X,
            Y = self.position.Y + self.height
        )

    def move_left(self):
        # self._position_x -= self.width
        self.position = SpritePosition(
            X = self.position.X - self.width,
            Y = self.position.Y
        )

    def move_right(self):
        # self._position_x += self.width
        self.position = SpritePosition(
            X = self.position.X + self.width,
            Y = self.position.Y
        )
    #endregion

    #region Touches Boundry
    def touches_boundry(self, field : WindowSize, direction : SnakeDirection) -> bool:
        match direction:
            case SnakeDirection.UP: return self._touches_top_boundry()
            case SnakeDirection.DOWN: return self._touches_bottom_boundry(field)
            case SnakeDirection.LEFT: return self._touches_left_boundry()
            case SnakeDirection.RIGHT: return self._touches_right_boundry(field)

    def _touches_top_boundry(self) -> bool:
        return self._position_y - self.height < 0

    def _touches_bottom_boundry(self, field : WindowSize) -> bool:
        return self._position_y + self.height >= field.HEIGHT

    def _touches_left_boundry(self) -> bool:
        return self.position.X - self.width < 0

    def _touches_right_boundry(self, field : WindowSize) -> bool:
        return self.position.X + self.width >= field.WIDTH
    #endregion

    def touches_apple(self, apple_position : SpritePosition) -> bool:
        return self.position.X == apple_position.X and self.position.Y == apple_position.Y
