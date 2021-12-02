from pathlib import Path
from math import floor
from configuration import Configuration, WindowSize
from sprites import Position, Block, Sprite
from typing import NamedTuple
from models.enum import SnakeSection, SnakeDirection, SnakeEvent

class Node(NamedTuple):
    name : str
    sprite : Sprite

class Snake:
    body : list[Node]
    _direction : SnakeDirection
    _block_path : Path
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
        self._land = config.window.WINDOW_SIZE
        self._block_path = config.sprites.BLOCK_PATH
        self._direction = SnakeDirection.RIGHT
        self.body = self._build_snake()

    def _build_snake(self) -> list[Node]:
        nodes : list[Node] = []
        for index in range(3):
            nodes.append(self._generate_node(index))
        return nodes
    
    def _generate_node(self, index : int) -> Node:
        block = Block(self._block_path)
        block.position = self._generate_block_position(index, block)
        return Node(name=self._get_nodename_by_index(index), sprite=block)
    
    def _generate_block_position(self, index : int, block : Block) -> Position:
        x_places = floor((self._land.WIDTH / block.surface.get_width()) / 2) * block.surface.get_width()
        y_places = floor((self._land.HEIGHT / block.surface.get_height()) / 2) * block.surface.get_height()
        diff = block.surface.get_width() * index
        return Position(
            X = x_places - diff, 
            Y = y_places
        )
    
    def _get_nodename_by_index(self, index : int) -> SnakeSection:
        if index == 0: return SnakeSection.HEAD
        elif index == [r for r in range(3)][-1]: return SnakeSection.TAIL
        else: return SnakeSection.SECTION
    
    def slither(self, direction : SnakeDirection = SnakeDirection.FORWARD) -> SnakeEvent:
        self.direction = direction
        if self.head.touches_boundry(self._land, self.direction):
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
