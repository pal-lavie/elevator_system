from enum import Enum

class CurrentState(Enum):
    MOVING_UP = 1
    MOVING_DOWN = 2
    STOPPED = 3
    IDLE = 4

class Floor(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10 
    