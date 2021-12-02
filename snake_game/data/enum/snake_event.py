from enum import Enum, auto

class SnakeEvent(Enum):
    MOVED = auto()
    HIT_WALL = auto()
