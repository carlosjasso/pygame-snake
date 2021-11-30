from enum import Enum, auto

class DisplayEvent(Enum):
    EXIT = auto()
    MOVE_UP = auto()
    MOVE_DOWN = auto()
    MOVE_LEFT = auto()
    MOVE_RIGHT = auto()

class SnakeSection(Enum):
    HEAD = auto()
    SECTION = auto()
    TAIL = auto()

class SnakeDirection(Enum):
    FORWARD = auto()
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

class SnakeEvent(Enum):
    MOVED = auto()
    HIT_WALL = auto()
