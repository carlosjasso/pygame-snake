from math import floor
from os import name
from pathlib import Path
from data.types import SpritePosition, SnakeNode, WindowSize
from data.enum import SnakeSection, SnakeDirection, SnakeEvent
from sprites import Block

class Snake:
    #region Attributes & Properties
    body : list[SnakeNode]
    _direction : SnakeDirection
    _block_path : Path
    _field : WindowSize

    @property
    def direction(self) -> SnakeDirection:
        return self._direction
    
    @direction.setter
    def direction(self, value : SnakeDirection):
        if value != self._direction and \
            value != SnakeDirection.FORWARD \
            and self._direction != self._get_counter_direction(value):
            self._direction = value

    @property
    def head(self) -> Block:
        return self.body[0].sprite
    
    @property
    def blocks(self) -> list[Block]:
        return [sprite for _, sprite in self.body]
    #endregion

    #region Init
    def __init__(self, window_size : WindowSize, img_path : Path):
        self._field = window_size
        self._block_path = img_path
        self._direction = SnakeDirection.RIGHT
        self.body = self._build_snake()

    def _build_snake(self) -> list[SnakeNode]:
        nodes : list[SnakeNode] = []
        for index in range(3):
            nodes.append(self._generate_node(index))
        return nodes
    
    def _generate_node(self, index : int) -> SnakeNode:
        block = Block(self._block_path)
        block.position = self._generate_block_position(index, block)
        return SnakeNode(name=self._get_nodename_by_index(index), sprite=block)
    
    def _generate_block_position(self, index : int, block : Block) -> SpritePosition:
        x_places = floor((self._field.WIDTH / block.surface.get_width()) / 2) * block.surface.get_width()
        y_places = floor((self._field.HEIGHT / block.surface.get_height()) / 2) * block.surface.get_height()
        diff = block.surface.get_width() * index
        return SpritePosition(
            X = x_places - diff, 
            Y = y_places
        )
    
    def _get_nodename_by_index(self, index : int) -> SnakeSection:
        if index == 0: return SnakeSection.HEAD
        elif index == [r for r in range(3)][-1]: return SnakeSection.TAIL
        else: return SnakeSection.SECTION
    #endregion
    
    #region Slither
    def slither(self, apple_position : SpritePosition, direction : SnakeDirection = SnakeDirection.FORWARD) -> SnakeEvent:
        self.direction = direction
        return self._process_event(apple_position)
    
    def _process_event(self, apple_position) -> SnakeEvent:
        if self.head.touches_boundry(self._field, self.direction) or self.touches_self():
            return SnakeEvent.CRASHED
        elif self.head.touches_apple(apple_position):
            return SnakeEvent.HIT_APPLE
        else: return self._slither()
    
    def _slither(self) -> SnakeEvent:
        position_pivot = self.head.position
        for node in self.body:
            position_pivot = self._update_node_position(node, position_pivot)
        return SnakeEvent.MOVED
    
    def _update_node_position(self, node : SnakeNode, pivot_position : SpritePosition):
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
    
    def _update_block_position(self, block : Block, previous_position : SpritePosition) -> SpritePosition:
        """
        Updates the block with the given position and returns the previous position value.
        """
        temp_position = block.position
        block.position = SpritePosition(previous_position.X, previous_position.Y)
        return temp_position
    #endregion

    #region Touches Self
    def touches_self(self) -> bool:
        match self.direction:
            case SnakeDirection.UP: return self._touches_self_up()
            case SnakeDirection.DOWN: return self._touches_self_down()
            case SnakeDirection.LEFT: return self._touches_self_left()
            case SnakeDirection.RIGHT: return self._touches_self_right()
    
    def _touches_self_up(self) -> bool:
        return len([b for b in self.blocks
            if b.position.X == self.head.position.X
            and b.position.Y == (self.head.position.Y - self.head.surface.get_height())]) > 0
    
    def _touches_self_down(self) -> bool:
        return len([b for b in self.blocks
            if b.position.X == self.head.position.X
            and b.position.Y == (self.head.position.Y + self.head.surface.get_height())]) > 0
    
    def _touches_self_left(self) -> bool:
        return len([b for b in self.blocks
            if b.position.X == (self.head.position.X - self.head.surface.get_width())
            and b.position.Y == self.head.position.Y]) > 0
    
    def _touches_self_right(self) -> bool:
        return len([b for b in self.blocks
            if b.position.X == (self.head.position.X + self.head.surface.get_width())
            and b.position.Y == self.head.position.Y]) > 0
    #endregion

    def grow_node(self):
        self.body[-1] = SnakeNode(name = SnakeSection.SECTION, sprite = self.body[-1].sprite)
        block = Block(self._block_path)
        block.position = self.body[-1].sprite.position
        self.body.append(SnakeNode(
            name = SnakeSection.TAIL,
            sprite = block
        ))

    #region Helpers
    def _get_counter_direction(self, direction : SnakeDirection) -> SnakeDirection:
        match direction:
            case SnakeDirection.UP: return SnakeDirection.DOWN
            case SnakeDirection.DOWN: return SnakeDirection.UP
            case SnakeDirection.LEFT: return SnakeDirection.RIGHT
            case SnakeDirection.RIGHT: return SnakeDirection.LEFT
    #endregion
