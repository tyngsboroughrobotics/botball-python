from ..helpers.enum import Enum


class Direction(Enum):
    """
    Represents the direction in which a motor/servo should move.
    """

    Forward = 1
    """
    The forward direction.
    """

    Backward = -1
    """
    The backward direction.
    """

    def multiplier(self) -> int:
        """
        Used by various internal functions to invert values in the case of a 
        backward direction.
        """
        return self.value
