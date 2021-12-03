from enum import Enum, auto

class SnakeEvent(Enum):
    MOVED = auto()
    CRASHED = auto()
    HIT_APPLE = auto()
