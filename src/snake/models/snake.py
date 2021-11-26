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
        node : Node = [node for node in self.body if node.name == SnakeSection.HEAD][0]
        return node.sprite
    
    @property
    def blocks(self) -> list[Block]:
        return [sprite for _, sprite in self.body]

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
            # snake gets built from tail to head
            if n == 0: name = SnakeSection.TAIL
            elif n == nodes[-1]: name = SnakeSection.HEAD
            else: name = SnakeSection.SECTION
            result.append(Node(name=name, sprite=block))
        return result
    
    def slither(self, direction : SnakeDirection = SnakeDirection.FORWARD):
        previous_position = self.head.position
        if direction != SnakeDirection.FORWARD and self.direction != direction:
            self.direction = direction
        for node in reversed(self.body):
            block : Block = node.sprite
            if node.name == SnakeSection.HEAD:
                match self.direction:
                    case SnakeDirection.UP: block.move_up()
                    case SnakeDirection.DOWN: block.move_down()
                    case SnakeDirection.LEFT: block.move_left()
                    case SnakeDirection.RIGHT: block.move_right()
            else:
                temp_position = block.position
                block.position_x = previous_position.x
                block.position_y = previous_position.y
                previous_position = temp_position
