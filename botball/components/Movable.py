from .Component import Component


class Movable(Component):
    """
    Implemented by both motors and servos. Provides a port and speed value.
    """

    speed: float
    """
    The speed of the motor between 0.0 (slowest) and 1.0 (fastest). 
    """

    def __init__(self, port: int, speed: float):
        super().__init__(port)

        if speed < 0.0 or speed > 1.0:
            raise ValueError("Speed must be between 0.0 and 1.0")

        self.speed = speed
