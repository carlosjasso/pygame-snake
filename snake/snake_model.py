from configuration import Configuration, WindowSize
from sprites import Position, Block, Sprite
from typing import NamedTuple
from enums import SnakeSection, SnakeDirection, SnakeEvent

class Node(NamedTuple):
    name : str
    sprite : Sprite

class Snake:
    config : Configuration
    body : list[Node]
    _direction : SnakeDirection
    _land : WindowSize

    @property
    def direction(self) -> SnakeDirection:
        return self._direction
    
    @direction.setter
    def direction(self, value : SnakeDirection):
        if value != self._direction and \
            value != SnakeDirection.FORWARD \
            and self._direction != self._get_coutner_direction(value):
            self._direction = value

    @property
    def head(self) -> Block:
        return self.body[0].sprite
    
    @property
    def blocks(self) -> list[Block]:
        return [sprite for _, sprite in self.body]

    def __init__(self, config : Configuration):
        self.config = config
        self._land = config.window.WINDOW_SIZE
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
        filler = int(self.config.window.WINDOW_SIZE.WIDTH / 2) - (block.surface.get_width() * 3)
        block.position = Position(
            X = block.surface.get_width() * (index) + filler,
            Y = int(self.config.window.WINDOW_SIZE.HEIGHT / 2) - block.surface.get_height()
        )
        return Node(name=self._get_nodename_by_index(index), sprite=block)
    
    def _get_nodename_by_index(self, index : int) -> SnakeSection:
        # snake gets built from tail to head
        if index == 0: return SnakeSection.TAIL
        elif index == [r for r in range(3)][-1]: return SnakeSection.HEAD
        else: return SnakeSection.SECTION
    
    def slither(self, direction : SnakeDirection = SnakeDirection.FORWARD) -> SnakeEvent:
        self.direction = direction
        if self.head.touches_boundry(self.config.window.WINDOW_SIZE, self.direction):
            return SnakeEvent.HIT_WALL
        else: return self._slither()
    
    def _slither(self) -> SnakeEvent:
        position_pivot = self.head.position
        for node in self.body:
            position_pivot = self._update_node_position(node, position_pivot)
        return SnakeEvent.MOVED
    
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
