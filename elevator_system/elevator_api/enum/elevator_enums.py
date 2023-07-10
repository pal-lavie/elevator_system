from enum import Enum

# Current state of elevator
class CurrentState(Enum):
    MOVING_UP = 1
    MOVING_DOWN = 2
    STOPPED = 3
    IDLE = 4

# Floor min and max values
class Floor(Enum):
    MAX_FLOOR = 10
    MIN_FLOOE = 1
    