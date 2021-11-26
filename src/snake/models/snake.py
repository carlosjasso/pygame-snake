from collections import namedtuple
from .configuration import Configuration
from .block import Block
from .snake_section import SnakeSection
from .snake_direction import SnakeDirection

Node = namedtuple("Node", ["name", "sprite"])

class Snake:
    config : Configuration
    body : set[Node]
    direction : SnakeDirection

    @property
    def head(self) -> Block:
        result : Node = self.body[SnakeSection.HEAD]
        return result.sprite

    def __init__(self, config : Configuration):
        self.config = config
        self.body = self._build_snake()
        self.direction = SnakeDirection.RIGHT

    def _build_snake(self) -> list[Node]:
        result : list[Node] = []
        nodes = [r for r in range(3)] # TODO: Change value to 1
        for n in nodes:
            name : str
            block = Block(self.config.sprites.BLOCK_PATH)
            block.position_x = block.surface.get_width() * (n)
            if n == 0: name = SnakeSection.HEAD
            elif n == nodes[-1]: name = SnakeSection.TAIL
            else: name = SnakeSection.SECTION
            result.append(Node(name=name, sprite=block))
        return result
    
