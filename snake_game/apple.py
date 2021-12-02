from sprites import Position
from configuration import Configuration, WindowSize
from sprites import Block

class Apple:
    _land : WindowSize
    _sprite : Block

    @property
    def sprite(self) -> Block:
        return self._sprite

    def __init__(self, configuration : Configuration) -> None:
        self._land = configuration.window.WINDOW_SIZE
        self._sprite = Block(configuration.sprites.APPLE_PATH)
        self._sprite.position = Position(0, 0)
