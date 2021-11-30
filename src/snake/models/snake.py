from .sprite import Position
from .configuration import Configuration
from .block import Block
from .enums.snake_section import SnakeSection
from .enums.snake_direction import SnakeDirection
from .types.node import Node

class Snake:
    config : Configuration
    body : list[Node]
    _direction : SnakeDirection

    @property
    def direction(self) -> SnakeDirection:
        return self._direction
    
    @direction.setter
    def direction(self, value : SnakeDirection):
        if value != SnakeDirection.FORWARD and self._direction != self._get_coutner_direction(value):
            self._direction = value

    @property
    def head(self) -> Block:
        return self.body[0].sprite
    
    @property
    def blocks(self) -> list[Block]:
        return [sprite for _, sprite in self.body]

    def __init__(self, config : Configuration):
        self.config = config
        self.body = self._build_snake()
        self._direction = SnakeDirection.RIGHT

    def _build_snake(self) -> list[Node]:
        nodes : list[Node] = []
        for index in range(3):
            nodes.append(self._generate_node(index))
        # Reverse nodes for head to be index 0
        return [n for n in reversed(nodes)]
    
    def _generate_node(self, index : int) -> Node:
        block = Block(self.config.sprites.BLOCK_PATH)
        block.position = Position(block.surface.get_width() * (index), 0)
        return Node(name=self._get_nodename_by_index(index), sprite=block)
    
    def _get_nodename_by_index(self, index : int) -> SnakeSection:
        # snake gets built from tail to head
        if index == 0: return SnakeSection.TAIL
        elif index == [r for r in range(3)][-1]: return SnakeSection.HEAD
        else: return SnakeSection.SECTION
    
    def slither(self, direction : SnakeDirection = SnakeDirection.FORWARD):
        self.direction = direction
        position_pivot = self.head.position
        for node in self.body:
            position_pivot = self._update_node_position(node, position_pivot)
    
    def _update_node_position(self, node : Node, pivot_position : Position):
        if node.name == SnakeSection.HEAD:
            self._update_head_position(node.sprite, self.direction)
            return pivot_position
        else:
            return self._update_block_position(node.sprite, pivot_position)
    
    def _update_head_position(self, block : Block, direction : SnakeDirection):
        match direction:
            case SnakeDirection.UP: block.move_up()
            case SnakeDirection.DOWN: block.move_down()
            case SnakeDirection.LEFT: block.move_left()
            case SnakeDirection.RIGHT: block.move_right()
    
    def _update_block_position(self, block : Block, previous_position : Position) -> Position:
        """
        Updates the block with the given position and returns the previous position value.
        """
        temp_position = block.position
        block.position = Position(previous_position.X, previous_position.Y)
        return temp_position

    def _get_coutner_direction(self, direction : SnakeDirection) -> SnakeDirection:
        match direction:
            case SnakeDirection.UP: return SnakeDirection.DOWN
            case SnakeDirection.DOWN: return SnakeDirection.UP
            case SnakeDirection.LEFT: return SnakeDirection.RIGHT
            case SnakeDirection.RIGHT: return SnakeDirection.LEFT
