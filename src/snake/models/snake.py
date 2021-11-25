from collections import namedtuple
from .block import Block
from .configuration import Configuration
from .snake_section import SnakeSection
from .snake_direction import SnakeDirection

Section = namedtuple("Section", ["name", "sprite"])

class Snake:
    config : Configuration
    body : set[Section]
    direction : SnakeDirection

    @property
    def head(self) -> Block:
        section : Section = self.body[SnakeSection.HEAD]
        return section.sprite

    def __init__(self, config : Configuration):
        self.config = config
        self.body = self._build_body()
        self.direction = SnakeDirection.RIGHT
    
    def _build_body(self) -> set[Section]:
        result = []
        sections = range(1)
        for s in sections:
            name : str
            if s == sections[0]: name = SnakeSection.HEAD
            elif s == sections[-1]: name = SnakeSection.TAIL
            else: name = SnakeSection.SECTION
            result.append(Section(name=name, sprite=Block(self.config.sprites.BLOCK_PATH)))
        return result

    def slither(self, direction = SnakeDirection.SAME):
        block = self.head
        if direction is not SnakeDirection.SAME:
            self.direction = direction
        match self.direction:
            case SnakeDirection.UP:
                block.move_up()
            case SnakeDirection.DOWN:
                block.move_down()
            case SnakeDirection.LEFT:
                block.move_left()
            case SnakeDirection.RIGHT:
                block.move_right()
